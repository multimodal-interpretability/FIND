import argparse
import openai
import regex

import pandas as pd
from getpass import getpass
import pandas as pd
from tqdm import tqdm
from IPython import embed
import time
from random import random, uniform
import warnings
warnings.filterwarnings("ignore")

# User inputs:
# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
# OR 
# Load your API key manually:
# openai.api_key = API_KEY

def ask_model(input,model,state):
    try:
        if model in ['gpt-3.5-turbo','gpt-4']:
            state.history.append({'role': 'user', 'content': input})
            r = openai.ChatCompletion.create(model=model, messages=state.history)
            resp = r['choices'][0]['message']['content']
            costFactor = [0.03, 0.06] if model == 'gpt-4' else [0.002, 0.002]
            state.totalCost += r['usage']['prompt_tokens']/1000*costFactor[0]+r['usage']['completion_tokens']/1000*costFactor[1]
            state.history.append({'role': 'assistant', 'content': resp})
        # TODO: add your model her:
        # if model == MY_MODEL:
        #   state.history.append({'role': 'user', 'content': input})
        #   resp = GET_YOUR_MODEL_RESPONSE
        #   state.history.append({'role': 'assistant', 'content': resp})
        else:
            print(f"Unrecognize model name: {model}")
            return 0
    except Exception as e:
        print(e)
        if model == 'gpt-3.5-turbo': return e
        time.sleep(30+30*random())
        resp = ask_model(input,model)
    return resp,state