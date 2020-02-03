# score_analysis

A python script that can be launched from the command line or in any python shell (e.g. IDLE: https://docs.python.org/3/library/idle.html). The program outputs answers to the questions:
1. Average score given by each evaluator
2. Average score for each sentence
3. The highest and lowest scoring sentences.

## Getting started
Download a copy of the program (score_analysis.py) and store it in the same location as the dataset (bulgarian-direct-assessment.csv). The location filepath of the csv file on the local machine must be specified inside the read_csv method at line 8.
If the csv file is located in the same folder as the program file, the program downloaded from the repository does not need to be modified.

The output file names are evaluator_mean.csv which answers question 1 above, sentence_mean.csv which answer question 2, and best_worst_sentences.txt which answers question 3.
The names of the files can be changed along with a location at lines 17, 26 and 41 respectively. 
Leaving them unchanged will create the files in the same location folder as the program.

## Prerequisites

Python 3.6 or later: https://www.python.org/downloads/.

Python packages: NumPy (http://www.numpy.org/), Pandas (https://pandas.pydata.org/).

## Installing

Install python3 and the above packages as described for your local environment at the above links.

Example for MacOS terminal/linux command line (using PIP, a python package manager that is included by default in releases greater than Python 3.4):

```
$ pip install pandas
```

```
$ pip install numpy
```

## Running the program

The program can be executed from the command line by navigating to the folder containing the program file (using cd command) and then executing the below command:

```
$ python score_analysis.py
```

Ensure the above is calling python3 by checking:

```
$ python --version
```

If your default is not set to python3, execute the program with the python3 command instead of python in the example line for running the program above.

## Results

The program will output the three files as outlined above.

The files containing the results of the program are included in the repository as evaluator_mean.csv which answers question 1 above, sentence_mean.csv which answer question 2, and best_worst_sentences.txt which answers question 3.

## Author
Conor Molumby

## License
Copyright 2020 Conor Molumby. This repository is provided under the MIT license (https://opensource.org/licenses/MIT).
