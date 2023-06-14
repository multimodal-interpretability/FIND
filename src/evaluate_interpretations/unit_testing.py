import argparse
import openai
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
import random
import json
import matplotlib.pyplot as plt
import sys 
import imp
import numpy as np
import math
import pandas as pd

random.seed(0000)

parser = argparse.ArgumentParser(description='Process Arguments')	
parser.add_argument('--model', type=str, default='gpt-4', help='interpreter model name to evaluate')	
parser.add_argument('--eval_model', type=str, default='gpt-4', help='model to use as an evaluator')	
parser.add_argument('--func_category', type=str, default='strings', help='function category')	
parser.add_argument('--test_path', type=str, default='../run_interpretations/results/', help='path to the interretations')	
parser.add_argument('--gt_path', type=str, default='../find_dataset/', help='path to the gt functions')	
parser.add_argument('--prompt_path', type=str, default='./utils/prompt_eval_strings.txt', help='path to the gt functions')	
parser.add_argument('--num_test', type=int, default=10, help='number of unit-testing triplets to test for each function')	
parser.add_argument('--num_func', type=int, default=5, help='number of functions to evaluate')	
parser.add_argument('--vicuna_temp', type=float, default=0, help='range to test the implementation:, the reange for input x is range(-x,x)')	
parser.add_argument('--vicuna_server', type=str, help='specify vicuna server address')	
parser.add_argument('--hints', action='store_true', help='add_search_initializations', default=False)

args = parser.parse_args()

sys_prompt = "You are a helpful assistant. You indicate which of the input-output mapping examples provided by the user is a possible execution of the function provided by the user. Answer with only the following format: '[ANSWER]: <index>' where <index> represent the numerical value of the correct example. Do not include any additional information in the answer."


def ask_model(system_instr,input,model='gpt-3.5-turbo',temp=0):
    try:
        if model in ['gpt-3.5-turbo','gpt-4']:
            resp = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": system_instr},{"role": "user", "content": input}])
            resp = resp['choices'][0]['message']['content']
        elif model in ['vicuna']:
            openai.api_key = "EMPTY"  # Not support yet
            openai.api_base = args.vicuna_server
            model = "vicuna-13b-v1.1"
            resp = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "system", "content": system_instr},{"role": "user", "content": input}],
                temperature=temp
            )
            resp = resp['choices'][0]['message']['content']
        else:
            print(f"Unrecognize model name: {model}")
            return 0
    except Exception as e:
        print(e)
        time.sleep(30+30*random.random())
        resp = ask_model(input,model)
    return resp

def return_test_prompt(desc,ins,outs=None):
    with open(args.prompt_path,'r') as f:
        prompt = f.read()
    prompt = prompt.replace('DESC',desc)
    if 'entities' in args.func_category:
        for i in range(len(ins)):
            prompt = prompt.replace(f'IN{i}',ins[i])
    else:
        for i in range(len(ins)):
            prompt = prompt.replace(f'IN{i}',ins[i])
            prompt = prompt.replace(f'OUT{i}',outs[i])
    return prompt

            
def main(args):
    t_start = time.time()
    counter = 0
    test_path_all = os.path.join(args.test_path,args.model,args.func_category)
    if args.hints:
        test_path_all = test_path_all + '_hints'
    if os.path.exists(os.path.join(test_path_all,f'test_res_data_{args.eval_model}.json')):
        with open(os.path.join(test_path_all,f'test_res_data_{args.eval_model}.json'), 'r') as file:
            test_data = json.load(file)
        with open(os.path.join(test_path_all,f'scores_{args.eval_model}.json'), 'r') as file:
            scores_all = json.load(file)
    else:
        test_data = []
        scores_all = []

    for function in tqdm(os.listdir(test_path_all)):
        fun_serial = int(function[1:])
        test_res = []
        test_path = os.path.join(test_path_all,function)
        if not os.path.isdir(test_path): continue

        with open(f'./utils/eval_data_{args.func_category}.json', 'r') as file:
            data_dict = json.load(file)
        test_vecs = data_dict[fun_serial]['test_vec']
        correct_inx = data_dict[fun_serial]['correct_inx']
        test_description = open(test_path+'/description.txt','r').read()

        count = 0
        for vec in test_vecs:
            if 'entities' in args.func_category:
                in_vec = vec
                prompt = return_test_prompt(test_description,in_vec) 
            else:
                in_vec = vec[0]
                out_vec = vec[1]
                prompt = return_test_prompt(test_description,in_vec,out_vec) 
            response = ask_model(sys_prompt,prompt,model=args.eval_model,temp=args.vicuna_temp) 
            if str(correct_inx[count]) in response: test_res.append(1)
            else: test_res.append(0)
            count+=1
       
        score = sum(test_res)/len(test_res)
        scores_all.append(score)
        data_curr = {'name': function,
                    'test_vec': test_vecs,
                    'correct_inx': correct_inx,
                    'results': test_res,
                    'score': score
                        }
        out_file = open(test_path+f'/test_res_{args.eval_model}.json', "w")
        json.dump(data_curr,out_file) 

        test_data.append(data_curr)
        with open(test_path_all+f'/test_res_data_{args.eval_model}.json', "w") as out_file:
            json.dump(test_data,out_file) 
        with open(test_path_all+f'/scores_{args.eval_model}.json', "w") as out_file:
            json.dump(scores_all,out_file) 
        
    t_end = time.time()
    print('mean score:',sum(scores_all)/len(scores_all))
    print(f'total time for {counter} functions: {t_end-t_start}')

if __name__ == '__main__':
    main(args)



