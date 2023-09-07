# FIND interpretation benchmark
# Run interpretations

### set OPENAI_API_KEY the environment variable
```export OPENAI_API_KEY= <YOUR_KEY>```

## Test interpretations 

### MSE indicator (for numeric functions)
```python mse_indicator.py```

### Unit-testing (for strings and synthetic neurons)

Download the vicuna-evaluator model:
```wget https://data.csail.mit.edu/FIND/vicuna_evaluator.zip```
(the training data is available at ```wget https://data.csail.mit.edu/FIND/vicuna_evaluator_train_data.json```)

For string functions:
```python unit_testing.py --func_category strings --prompt_path ./utils/prompt_eval_strings.txt```

For synthetic neurons - entities:
```python unit_testing.py --func_category neurons_entities --prompt_path ./utils/prompt_eval_entities.txt```
includ the flag `--hints` to evaluate interpretation with search initialization. 

For synthetic neurons - relations:
```python unit_testing.py --func_category neurons_relations --prompt_path ./utils/prompt_eval_relations.txt```
includ the flag `--hints` to evaluate interpretation with search initialization. 
