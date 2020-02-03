#import pandas as pd
import pandas as pd

#import numpy as np
import numpy as np

#read in csv file of raw data
df_raw = pd.read_csv('bulgarian-direct-assessment.csv')

#create dataframe of average score per evaluator
df_evaluator_mean = df_raw.groupby(['evaluator id'], as_index=False).mean().round(2)

#rename score column to include mean
df_evaluator_mean = df_evaluator_mean.rename(columns={'score': 'mean_score'})

#output evaluator mean scores to csv
df_evaluator_mean.to_csv('evaluator_mean.csv', index=False)

#create dataframe of average score per sentence
df_sentence_mean = df_raw.groupby(['sentence pair id'], as_index=False).mean().round(2)

#rename score column to include mean
df_sentence_mean = df_sentence_mean.rename(columns={'score': 'mean_score'})

#output mean sentence scores to csv
df_sentence_mean.to_csv('sentence_mean.csv', index=False)

#get id of highest scoring sentence
max_sentence_id = str(df_sentence_mean['sentence pair id'].loc[df_sentence_mean['mean_score'] == df_sentence_mean['mean_score'].max()].iloc[0])

#get text of highest scoring sentence
max_sentence_text = df_raw['original'].loc[df_raw['sentence pair id'] == max_sentence_id].iloc[0]

#get id of lowest scoring sentence
min_sentence_id = str(df_sentence_mean['sentence pair id'].loc[df_sentence_mean['mean_score'] == df_sentence_mean['mean_score'].min()].iloc[0])

#get text of lowest scoring sentence
min_sentence_text = df_raw['original'].loc[df_raw['sentence pair id'] == min_sentence_id].iloc[0]

#Output the result to a text file:
with open("best_worst_sentences.txt", 'w') as txt_file1:
    print('Best sentence id: ' + max_sentence_id +'.\n'
          'Best sentence: ' + max_sentence_text + '\n'
          'Worst sentence id: ' + min_sentence_id + '.\n'
          'Worst sentence: ' + min_sentence_text + '\n', file=txt_file1)
