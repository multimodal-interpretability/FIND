import openai
import sys
import numpy as np
import torch

openai.api_key = "EMPTY"  # Not support yet
openai.api_base = {API_BASE}
model = "vicuna-13b-v1.1"

from transformers import LlamaTokenizer
tokenizer = LlamaTokenizer.from_pretrained({LLAMA_PATH})
zero_token_id = tokenizer._convert_token_to_id('0')  # 29900
one_token_id = tokenizer._convert_token_to_id('1')  # 29896

concept = 'elections'

def function(input, sys_prompt):
    messages=[
        {"role": "system", "content": sys_prompt},   #system prompt
        {"role": "user", "content": 
        f"I am going to give you an input. Return only \"1\" if that input is related to {concept}. "+
         "Return only \"0\" otherwise.\nDo not return any additional information other than the 0 or 1 answer.\n"+
         f"Input: {input}"}
    ]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0
    )

    logprobs = np.array(completion.choices[0].logprobs)
    output_tokens = tokenizer.encode(completion.choices[0].message.content, return_tensors='pt')
    indices_of_zero_or_one = torch.logical_or(output_tokens == zero_token_id, output_tokens == one_token_id)
    indices_of_zero_or_one = indices_of_zero_or_one.int()
    index_of_choice = indices_of_zero_or_one.nonzero()
    index = index_of_choice[0][1].item()
    index = index-1
    prob_1 = np.exp(logprobs[index, one_token_id]) / (np.exp(logprobs[index, zero_token_id]) + np.exp(logprobs[index, one_token_id]))

    return prob_1 

if __name__ == '__main__':
    outputs = ''
    prompt = "You are an AI trained to identify words related to input concepts."
    for arg in sys.argv[1:]:
        outputs += f'({arg}, {function(arg, prompt):.4f}) '
    print(f'Function input - output pairs: {outputs}')