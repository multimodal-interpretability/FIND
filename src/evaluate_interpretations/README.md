# FIND interpretation benchmark
# Run interpretations

### dataset
If you wish to use FIND functions for evaluation, download and unzip the FIND dataset into `./src/find-dataset`:

```bash
wget -P ./src/find_dataset/ https://zenodo.org/record/8039658/files/FIND-dataset.zip
unzip ./src/find_dataset/FIND-dataset.zip -d ./src/
```
We include the dataset structure and examples of 5 functions per category under `./src/find_dataset/`

If you whish to test FIND interpretations, download the full FIND interpretations benchmark and unzip it to `./src/run_interpretations/`:
```bash
wget -P ./src/run_interpretations https://data.csail.mit.edu/FIND/FIND-interpretations.zip
unzip ./src/run_interpretations/FIND-interpretations.zip -d ./src/run_interpretations/
```

## Test interpretations 

### Code based - MSE indicator (for numeric functions)
```python mse_indicator.py```

### Code based - string indicator (for string functions approximation)
```python string_indicator.py```

### Language based - unit testing (for strings and synthetic neurons)

Download the vicuna-evaluator model:

```wget https://data.csail.mit.edu/FIND/vicuna_evaluator.zip```

(the training data is available at: 
```wget https://data.csail.mit.edu/FIND/vicuna_evaluator_train_data.json```)

Install FastChat and the OpenAI API

```bash
pip install fschat
pip install openai
```

Then start serving vicuna-evaluator (run these three commands separately):

```bash
python -m fastchat.serve.controller
python -m fastchat.serve.model_worker --model-name 'vicuna-13b-v1.1' --model-path /path/to/vicuna-evaluator --num-gpus 2
python -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 8000
```

For string functions:
```python unit_testing.py --func_category strings --prompt_path ./utils/prompt_eval_strings.txt --eval_data_path ../find_dataset/strings/unit_test_data.json```

For synthetic neurons - entities:
```python unit_testing.py --func_category neurons_entities --prompt_path ./utils/prompt_eval_entities.txt --eval_data_path ../find_dataset/neurons_entities/unit_test_data.json```
include the flag `--hints` to evaluate interpretation with search initialization. 
include the flag `--single_round` for the MILAN settings. 

For synthetic neurons - relations:
```python unit_testing.py --func_category neurons_relations --prompt_path ./utils/prompt_eval_relations.txt --eval_data_path ../find_dataset/neurons_relations/unit_test_data.json```
include the flag `--hints` to evaluate interpretation with search initialization. 
include the flag `--single_round` for the MILAN settings. 