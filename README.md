# FIND: Function Interpretation and Description Benchmark
**A Function Interpretation Benchmark for Evaluating Interpretability Methods (official implementation)** <br>
### [Project Page](https://multimodal-interpretability.csail.mit.edu/FIND-benchmark/) | [Arxiv](https://arxiv.org/abs/2309.03886)

[Sarah Schwettmannn](https://cogconfluence.com/)\*, [Tamar Rott Shaham](https://tamarott.github.io/)\*, [Joanna Materzynska](https://joaanna.github.io/), [Neil Chowdhury](https://nchowdhury.com/), [Shuang Li](https://people.csail.mit.edu/lishuang/), [Jacob Andreas](https://www.mit.edu/~jda/), [David Bau](https://baulab.info/), [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/). <br>
\* equal contribution <br><br>
![FIND overview](/assets/FIND_overview.png)

**This repository is under active development, expect updates!** <br>

## Setup

Clone this repository:
```bash
git clone https://github.com/multimodal-interpretability/FIND
cd FIND
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Then download and unzip the FIND dataset into `./src/find-dataset`:


```bash
wget -P ./src/find_dataset/ https://zenodo.org/record/8039658/files/FIND-dataset.zip
unzip ./src/find_dataset/FIND-dataset.zip -d ./src/
```
We include the dataset structure and examples of 5 functions per category under `./src/find_dataset/`

## Run interpretations
To run the interpretation, run `cd ./src/run_interpretations/` and follow the instructions on the README file. 
The code will also allow you to add your own interpreter model.

You can also download the full FIND interpretations benchmark and unzip it to `./src/run_interpretations/`:
```bash
wget -P ./src/run_interpretations https://data.csail.mit.edu/FIND/FIND-interpretations.zip
unzip ./src/run_interpretations/FIND-interpretations.zip -d ./src/run_interpretations/
```

See interpretation examples at `./src/notebooks/example_interpretations.ipynb`

## Evaluate interpretations
To evaluate the interpretations, run `cd ./src/evaluate_interpretations/` and follow the instructions on the README file. 

## Generate new functions
To generate a new set of numeric and/or strings functions, run `cd ./src/make_functions/` and follow the instructions on the README file. 
