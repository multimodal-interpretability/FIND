# FIND interpretation benchmark
# Run interpretations

## set OPENAI_API_KEY the environment variable
```export OPENAI_API_KEY= <YOUR_KEY>```

## Collect interpretations from gpt-4 and gpt-3.5-turbo

### Numeric functions
```python collect_interpretations.py --func_category numeric --prompt_path ./prompts/numeric.txt```

### Strings functions
```python collect_interpretations.py --func_category strings --prompt_path ./prompts/strings.txt```

## Synthetic neurons - entities
Install FastChat and the OpenAI API
```bash
pip install fschat
pip install openai
```
Follow [these instructions](https://huggingface.co/docs/transformers/main/model_doc/llama) to download the llama-13b weights and install dependencies. Then download vicuna-13b delta weights from [here](https://github.com/lm-sys/FastChat#vicuna-weights).
Then start serving Vicuna-13b (run these three commands separately):
```bash
python -m fastchat.serve.controller
python -m fastchat.serve.model_worker --model-name 'vicuna-13b-v1.1' --model-path /path/to/vicuna-13b --num-gpus 2
python -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 8000
```
(this is only needed for synthetic neurons functions)

Run interpretations:
```python collect_interpretations.py --func_category neurons_entities --prompt_path ./prompts/neurons_entities.txt --vicuna_server <vicuna_server> --llama_hf_path <llama_path>```

Run interpretations with search initialization:
```python collect_interpretations.py --func_category neurons_entities --prompt_path ./prompts/neurons_entities.txt --vicuna_server <vicuna_server> --llama_hf_path <llama_path> --hints```


## Synthetic neurons - relations
Lanch vicuna (see instructions in the entities function above).
Run interpretations:
```python collect_interpretations.py --func_category neurons_relations --prompt_path ./prompts/relations.txt --vicuna_server <vicuna_server>```
Run interpretations with search initialization:
```python collect_interpretations.py --func_category neurons_relations --prompt_path ./prompts/relations.txt --vicuna_server <vicuna_server> --hints```

## Define your own interpreter
Open the `collect_interpretations.py` function and define your model according to the instructions.