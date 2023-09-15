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
parser.add_argument('--func_category', type=str, default='numeric', help='function category')	
parser.add_argument('--test_path', type=str, default='../run_interpretations/results/', help='path to the interretations')	
parser.add_argument('--gt_path', type=str, default='../find_dataset/', help='path to the gt functions')	
parser.add_argument('--test_range', type=float, default=128, help='range to test the implementation:, the reange for input x is range(-x,x)')	
parser.add_argument('--nmse_threshold', type=float, default=0.1, help='threshold for the NMSE indicator')	
parser.add_argument('--nfunc', type=int, default=1000, help='number of functions')	
args = parser.parse_args()

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

           
def main(args):
    t_start = time.time()
    counter = 0
    test_path_all = os.path.join(args.test_path,args.model,args.func_category)
    gt_path_all = os.path.join(args.gt_path,args.func_category)
    if os.path.exists(os.path.join(test_path_all,'test_res_data.json')):
        with open(os.path.join(test_path_all,'test_res_data.json'), 'r') as file:
            test_data = json.load(file)
        with open(os.path.join(test_path_all,'scores.json'), 'r') as file:
            scores_all = json.load(file)
    else:
        test_data = []
        scores_all = []

    # for function in tqdm(os.listdir(test_path_all)):
    for function_ind in tqdm(range(args.nfunc)):
        function = f"f{function_ind:05d}"
        if os.path.isfile(os.path.join(test_path_all,function)): continue 
        path2save = os.path.join(test_path_all,function,'test/')
        os.makedirs(path2save,exist_ok=True)
        path2gt_func = os.path.join(gt_path_all,function,'function_code.py')
        path2test_func = os.path.join(test_path_all,function,'code.py')
        x = range(-args.test_range, args.test_range)
        func_gt = imp.load_source('function', path2gt_func)
        test_func_name = get_test_func_name(path2test_func)
        test_out = []
        gt_out = []
        x2plot = []
        try:
            func_test = imp.load_source(test_func_name, path2test_func)
            for i in x:
                gt_val = func_gt.function(float(i+0.5))
                if (not math.isnan(abs(gt_val))) and (not math.isinf(abs(gt_val))):
                    gt_out.append(gt_val)
                    exec(f"test_out.append(func_test.{test_func_name}({i+0.5}))")
                    x2plot.append(i+0.5)
            mse,normlized_mse = list_mse(gt_out,test_out)
            if normlized_mse<args.nmse_threshold: score = 1
            else: score = 0
            scores_all.append(score)
            # plot the result
            plt.plot(x2plot, gt_out, label='gt')
            plt.plot(x2plot, test_out, label=args.model)
            plt.legend()
            plt.savefig(f'{path2save}/test.png')
            plt.close()
        except:
            score = 0
            mse = None
            normlized_mse = None
            scores_all.append(score)

        data_curr = {'name': function,
                    'mse': mse,
                    'nmse': normlized_mse,
                    'score': score} 
        
        test_data.append(data_curr)

        with open(test_path_all+'/test_res_data.json', "w") as out_file:
            json.dump(test_data,out_file) 
        with open(test_path_all+'/scores.json', "w") as out_file:
            json.dump(scores_all,out_file) 
        counter+=1

    print(f'#NMSE<thresh: {sum(scores_all)/len(scores_all)}')

    t_end = time.time()
    print(f'total time for {counter} functions: {t_end-t_start}')

if __name__ == '__main__':
    main(args)



