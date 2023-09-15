import openai
import sys

openai.api_key = "EMPTY"  # Not support yet
openai.api_base = {API_BASE}
model = "vicuna-13b-v1.1"

con1 = 'a monument'
con2 = 'the continent where that monument is located'

def function(input, sys_prompt):
    messages=[
        {"role": "system", "content": sys_prompt},   #system prompt
        {"role": "user", "content": 
         f"I am going to give you an input." + 
         f"If the input is {con1}, reply with only {con2}. " + 
         f"If the input is not {con1}, return 'undefined'.\n"+
         f"Do not include any additional information other than the output.\n"+
         f"Input:{input}"
         }
    ]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0
    )

    return completion.choices[0].message.content

if __name__ == '__main__':
    outputs = ''
    prompt = "You are a helpful assistant. You apply real-world knowledge to map input words to output words according to a rule provided by the user. Try to be as precise as possible. Do not include additional explanation."
    for arg in sys.argv[1:]:
        x = arg
        outputs += f'({arg}, {function(arg, prompt)}) '
    print(f'Function input - output pairs: {outputs}')