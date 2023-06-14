# some code parts are based on the functions provided by the repo:
# https://github.com/d3n7/GPT-4-Unlimited-Tools

import argparse
# import openai
import regex
import re
import pandas as pd
import subprocess
from getpass import getpass
import pandas as pd
import os
from tqdm import tqdm
from IPython import embed
import time
from random import random, uniform
import random as rd
import torch.nn as nn
import json
import warnings
# warnings.filterwarnings("ignore")
import numpy as np
from call_interpreter import ask_model
rd.seed(0000)

parser = argparse.ArgumentParser(description='Process Arguments')	
parser.add_argument('--model', type=str, default='gpt-4', help='model name')	
parser.add_argument('--func_category', type=str, default='numeric', help='function category')	
parser.add_argument('--debug', action='store_true', help='debug mode, print dialogues to screan', default=False)
parser.add_argument('--dataset_path', type=str, default='./results/', help='a path to save the model outputs')	
parser.add_argument('--function_path', type=str, default='../find_dataset/', help='path to the gt functions')	
parser.add_argument('--temp_function_path', type=str, default='./temp/', help='path to copy the gt functions')	
parser.add_argument('--prompt_path', type=str, default='./prompts/numeric.txt', help='path to prompt to use')	
parser.add_argument('--n_func', type=int, default=5, help='specify the amount of functions to run')	
parser.add_argument('--vicuna_server', type=str, help='specify vicuna server address')	
parser.add_argument('--llama_hf_path', type=str, help='specify vicuna server address')	
parser.add_argument('--hints', action='store_true', help='add_search_initializations', default=False)
args = parser.parse_args()

regx = [r"([A-Z]+\(((?:[^()\"']|(?:\"[^\"]*\")|(?:'[^']*')|\((?1)*\))*)\))",
        r'''(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|\b[^,]+)''']

class SessionState:
    def __init__(self):
        self.running = False
        self.followup = False
        self.prompt = ''
        self.command = ''
        self.acceptreject = False
        self.history = []
        self.totalCost = 0
        self.displayChat = False
        self.displayCost = False

newSession =  True
manualApproval = False

def followup(state):
    state.followup, state.running = True, True

def formatTable(table):
    lines = ''
    for x, i in enumerate(table['GPT Commands']):
        lines += '{} - {}\n'.format(table['GPT Commands'][x],table['GPT Explanations'][x])
    return(lines)

commandTable = pd.DataFrame({
    'GPT Commands': ['PYTHON(function.py)'],
    'GPT Explanations': ['Run a python script with the given file name. Use quotes for the filename argument. Do not use quotes in the function command itself.'],
    'Raw Translation': ['python {}']
})

# return the prompt according to the task
def return_sysPrompt(model):
    if model == 'gpt-4':
        sysPrompt = 'You now have access to some commands to help complete the user\'s request. ' \
            'You are able to access the user\'s machine with these commands. In every message you send, ' \
            'include "COMMAND: " with your command at the end. Here is a list of commands with ' \
            'explanations of how they are used:\n{}\n When you use a command, the user will respond ' \
            'with "Response: " followed by the output of the commmand. Use this output to help the ' \
        'user complete their request.'
    else:
        sysPrompt = 'You now have access to some commands to help complete the user\'s request. ' \
        'You are able to access the user\'s machine with these commands, and to get the corresponding output from the user. ' \
        'In every message you send, ' \
        'include "COMMAND: " with your command at the end. ' \
        'When you use a command, the user will respond ' \
        'with "Response: " followed by the output of the commmand.' \
        'Do not run anything yourself. Only state the command and wait for the user to provide its output. ' \
        'Use this output to help the ' \
        'user complete their request. ' \
        'Here is a list of commands with ' \
        'explanations of how they are used:\n{}\n ' \
        '(Let the user provide the respones for your commands, do not estimate them yourself without feedback from the user).' \
        # 'Do not run anything yourself. Only state the command. ' \   
    return sysPrompt

def runCmd(flag,state):
    if flag:
        try:
            p = subprocess.Popen(state.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, errors = p.communicate()
            state.prompt = 'Response: ' + output.decode("utf-8")
            # print(output.decode("utf-8"))
            if errors:
                state.prompt += 'Error occurred, please try again (some of the input values might be undefined)'
                # state.prompt += 'Errors: ' + errors.decode("utf-8")
        except subprocess.CalledProcessError as e:
            state.prompt = 'Response: ' + e.output.decode("utf-8")
    else:
        state.prompt = "Response: User rejected this command"
    followup(state)

def define_prompt(prompt_template,dir2func):
    prompt = prompt_template.format(DIR2FUNC=os.path.join(dir2func))
    return prompt

def save_description(response, filepath):
    description = response.rsplit('[DESCRIPTION]: ')[-1]
    description = description.rsplit('[DOMAIN]: ')[0]
    with open(filepath,'w') as f:
        f.write(description) 
    f.close()   

def save_domain(response,filepath):
    domain = response.rsplit('[DOMAIN]: ')[-1]
    domain = domain.rsplit('[CODE]:')[0]
    with open(filepath,'w') as f:
        f.write(domain) 
    f.close()

def save_code(response,filepath):
    code = response.rsplit('[CODE]:')[-1]
    if code.find('```python') != -1:
        code = code.rsplit('```python')[-1]
        code = code.rsplit('```')[0]
    elif code.find('``` python') != -1:
        code = code.rsplit('``` python')[-1]
        code = code.rsplit('```')[0]
    elif code.find('```') != -1:
        code = code.rsplit('```',maxsplit=2)[1]
    else:
        code = ''
        
    with open(filepath,'w') as f:
        f.write(code) 
    f.close()

def save_fullhistory(history,filepath):
    with open(filepath+'.txt', 'a') as f:
        for i in history:
            if i['role'] == 'user':
                f.write('\nuser:\n'+i['content'])
            elif i['role'] == 'assistant':
                f.write('\nassistant:\n'+i['content'])
    with open(filepath+'.json', 'w') as file:
        json.dump(history, file)
    f.close()


def interp_func(prompt,model,debug=False):
    state = SessionState()
    sysPrompt = return_sysPrompt(model)
    round_count = 0
    while True:
        state.running = True
        if state.running:
            state.running = False 
            if not state.followup:
                state.prompt = prompt
            if (newSession or state.history == []) and (not state.followup):
                state.history = [{'role': 'system', 'content': sysPrompt.format(formatTable(commandTable))}]
            else:
                state.history[0] = {'role': 'system', 'content': sysPrompt.format(formatTable(commandTable))}
            state.followup = False 
            response,state = ask_model(state.prompt, model, state)
            if len(regex.findall(regx[0], response)) >= 1:
                cmd = regex.findall(regx[0], response)[0][0]
                pIndex = cmd.index('(')
                stem = cmd[:pIndex]
                rawArgs = cmd[pIndex+1:][:-1]
                cmdId = -1

                for x, i in enumerate(commandTable['GPT Commands']):
                    if stem in i:
                        cmdId = x
                        break

                rawArgs.replace('\n', '\\n')
                rawArgs.replace('\\\n', '\\n')
                if cmdId == -1:
                    state.prompt = 'Response: Unrecognized command'
                    followup(state)
                elif "'''" in rawArgs:
                    state.prompt = 'Response: Error parsing multi-line string (\'\'\') Use a single line with escaped newlines instead (")'
                    followup(state)
                elif '"""' in rawArgs:
                    state.prompt = 'Response: Error parsing multi-line string (\"\"\") Use a single line with escaped newlines instead (")'
                    followup(state)
                else:
                    state.command = commandTable['Raw Translation'][cmdId]
                    args = []
                    if rawArgs != '':
                        args =  re.findall(regx[1], rawArgs) #[rawArgs]
                        state.command = state.command.format(*args)

                    singleQuotes = False
                    for i in args:
                        if i.startswith("'"):
                            singleQuotes = True
                            state.prompt = "Response: Error parsing argument in single quotes. Use double quotes around the argument instead"
                            followup(state)
                            break

                    if not singleQuotes:
                        if manualApproval:
                            state.acceptreject = False
                        else:
                            runCmd(1,state)

        # round_count+=1
                    
        if state.acceptreject:
            print('GPT is trying to run the following command: ' + state.command + '\nPlease accept or reject this request.')
            decision = input('Accept or Reject [Accept, Reject]:')
            if decision.lower() == 'accept':
                state.acceptreject = False
                runCmd(1,state)
            elif decision.lower() == 'reject':
                state.acceptreject = False
                runCmd(0,state)

        if debug:
            print(response)                
            print(state.prompt)
            
        if "[DESCRIPTION]" in response:
            # print('')
            return(response,state.history)  

        if round_count>100:
            raise Warning("Interpretation process exceeded 100 rounds")
            return('','')    
        
def copy_func(source,target,category,vicuna_server=None,llama_hf_path=None):
    func_name = 'function_code.py'
    if 'numeric' in args.func_category:
        if os.path.exists(f'{source}/mlp_approx_model.pt'):
            # os.system(f'rm {target}/mlp_approx_model.pt')
            os.system(f'scp {source}/mlp_approx_model.pt {target}/mlp_approx_model.pt')
    if ('neurons_entities' in category) or ('neurons_relations' in category):
        temp = open(f'{source}/{func_name}','r').read()
        temp = temp.replace('{API_BASE}',f"'{vicuna_server}'")
        temp = temp.replace('{LLAMA_PATH}',f"'{llama_hf_path}'")
        open(target+'/function.py','w').write(temp)
    else:
        os.system(f'scp {source}/{func_name} {target}/function.py')
    return


def remove_func(target):
    os.system(f'rm {target}')

def remove_temp_folder(target):
    os.system(f'rm -r {target}')


def main(args):
    with open(args.prompt_path,'r') as f:
        prompt_template = f.read()
    # os.mkdir(os.path.join(args.dataset_path,args.model,args.func_category))
    t_start = time.time()
    count = 0   
    remove_temp_folder(args.temp_function_path)
    os.makedirs(args.temp_function_path, exist_ok=True)
    for function in tqdm(os.listdir(args.function_path+args.func_category)): 
        if count >= args.n_func: break
        path2save = os.path.join(args.dataset_path,args.model,args.func_category,function)
        if args.hints:
            path2save = os.path.join(args.dataset_path,args.model,args.func_category+'_hints',function)
        if os.path.exists(path2save+'/description.txt'): continue
        
        os.makedirs(path2save, exist_ok=True)
        mlp_flag = False
        if 'numeric' in args.func_category:
            if int(function[1:]) < 150:
                mlp_flag = True
        copy_func(source=os.path.join(args.function_path,args.func_category,function),target=args.temp_function_path,category=args.func_category,vicuna_server=args.vicuna_server,llama_hf_path=args.llama_hf_path)
        prompt = define_prompt(prompt_template,args.temp_function_path+'function.py')
        if args.hints:
            initial = open(os.path.join(args.function_path,args.func_category,function,'initial.json'),'r').read()
            prompt += f'\nWe advise you to start with the following words: {initial}'
        if mlp_flag:
            prompt_path_mlp = args.prompt_path.replace('numeric','numeric_mlp')
            with open(prompt_path_mlp,'r') as f:
                prompt_template_mlp = f.read()
            prompt = define_prompt(prompt_template_mlp,args.temp_function_path+'function.py')
        if args.debug:
            print(prompt)
        while True:
            try:
                response,history = interp_func(prompt,args.model,args.debug)
                break
            except Exception as e:
                print(e)
        save_fullhistory(history,path2save+'/history')
        save_description(response,path2save+'/description.txt')
        if ('numeric' in args.func_category) or ('neurons' in args.func_category):
            save_domain(response,path2save+'/domain.txt')
        if 'numeric' in args.func_category:
            save_code(response,path2save+'/code.py')
            if mlp_flag:
                os.system(f'rm {args.temp_function_path}/mlp_approx_model.pt')
        remove_func(args.temp_function_path+'function.py')
        count+=1
        
    t_end = time.time()
    print(f'total time for {count} functions: {t_end-t_start}')
    remove_temp_folder(args.temp_function_path)

if __name__ == '__main__':
    main(args)



