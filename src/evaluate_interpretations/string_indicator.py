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
from random import random
import json
import matplotlib.pyplot as plt
import sys 
import imp
import numpy as np
import math

parser = argparse.ArgumentParser(description='Process Arguments')	
parser.add_argument('--model', type=str, default='gpt-4', help='model name')	
parser.add_argument('--func_category', type=str, default='strings', help='function category')	
parser.add_argument('--test_path', type=str, default='../run_interpretations/results/', help='path to the interretations')		
parser.add_argument('--eval_data_path', type=str, default='./utils/eval_data_strings.json', help='path to the interretations')	
parser.add_argument('--nfunc', type=int, default=1000, help='number of functions')	
args = parser.parse_args()


with open(args.eval_data_path, 'r') as file:
    data_dict = json.load(file)

def list_mse(x,y):
    mse = []
    normalization = []
    for i in range(len(x)):
        mse.append(abs(x[i]-y[i])**2)
        normalization.append(abs(x[i])**2)
    return sum(mse)/len(mse), sum(mse)/sum(normalization)


def get_test_func_name(path):
    f = open(path,'r')
    test_code = f.read()
    if test_code == '': return ''
    test_func_name = test_code.rsplit('def ')[-1]
    test_func_name = test_func_name.rsplit('(')[0]
    return test_func_name

def get_test_val(fun_serial):
    test_vecs = data_dict[fun_serial]['test_vec']
    correct_inx = data_dict[fun_serial]['correct_inx']
    return test_vecs,correct_inx

def main(args):
    t_start = time.time()
    counter = 0
    test_path_all = os.path.join(args.test_path,args.model,args.func_category)
    test_data = []
    scores_all = []

    # for function in tqdm(os.listdir(test_path_all)):
    for function_ind in tqdm(range(args.nfunc)):
        function = f"f{function_ind:05d}"
        if os.path.isfile(os.path.join(test_path_all,function)): continue 
        # path2save = os.path.join(test_path_all,function,'test/')
        # os.makedirs(path2save,exist_ok=True)
        # if test_func_name == '':
        #     continue
        score = []
        try:
            path2test_func = os.path.join(test_path_all,function,'code.py')
            test_vecs,correct_inx = get_test_val(int(function[1:]))
            test_func_name = get_test_func_name(path2test_func)
            func_test = imp.load_source(test_func_name, path2test_func)
            for inx, vec in enumerate(test_vecs):
                test_out = []
                curr_correct_inx = int(correct_inx[inx])-1
                in_val = str(vec[0][curr_correct_inx])
                out_val = vec[1][curr_correct_inx]
                exec(f"test_out.append(func_test.{test_func_name}(\'{in_val}\'))")
                if out_val==test_out[0]: score.append(1)
                else: score.append(0)
        except:
            score.append(0)

        scores_all.append(sum(score)/len(score))

        data_curr = {'name': function,
                    'score': score} 
        
        test_data.append(data_curr)

        with open(test_path_all+'/test_res_data_code.json', "w") as out_file:
            json.dump(test_data,out_file) 
        with open(test_path_all+'/scores_code.json', "w") as out_file:
            json.dump(scores_all,out_file) 
        counter+=1

    print(f'score: {sum(scores_all)/len(scores_all)}')

    t_end = time.time()
    print(f'total time for {counter} functions: {t_end-t_start}')

if __name__ == '__main__':
    main(args)



