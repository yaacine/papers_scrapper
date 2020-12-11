# %matplotlib inline

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import random

# get the folder that contains the cleaned csv files 
foldername= input('Introduce the name of the cleaned folder, eg: 2_17 :  ')
papers_datasets = pd.read_csv('datasets/cleaned/'+foldername+'/articles_'+foldername+'_clean.csv')

# get the number of topics from the user 
nb_topics_str = input('Itroduce the number of Topics to use in LDA (recommanded 10 percent of the number of papers in the dataset) : ')
nb_topics = int(nb_topics_str)

papers_datasets = papers_datasets.head(20000)
papers_datasets.dropna()


count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = count_vect.fit_transform(papers_datasets['abstract'].values.astype('U'))


LDA = LatentDirichletAllocation(n_components=nb_topics, random_state=42)
LDA.fit(doc_term_matrix)

# TODO: uncommant this section if you want to see the outputs (not recommanded ✌️)
# for i in range(10):
#     random_id = random.randint(0,len(count_vect.get_feature_names()))
#     print(count_vect.get_feature_names()[random_id])


first_topic = LDA.components_[0]
top_topic_words = first_topic.argsort()[-10:]
# TODO: uncommant this section if you want to see the outputs (not recommanded ✌️)
# for i in top_topic_words:
#     print(count_vect.get_feature_names()[i])

topics = {}
for i,topic in enumerate(LDA.components_):
    topics[i]=[count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]]
    # TODO: uncommant this section if you want to see the outputs (not recommanded ✌️)
    # print(f'Top 10 words for topic #{i}:')
    # print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    # print('\n')

topic_values = LDA.transform(doc_term_matrix)
topic_values.shape


# save the new dataframe that includes topics into another file 
reviews_datasets['Topic'] = topic_values.argmax(axis=1)
reviews_datasets.to_csv('datasets/cleaned/'+foldername+'/articles_'+foldername+'_clean_topic.csv')

# save the topics into another file
df = pd.DataFrame.from_dict(topics, orient="index")
df.to_csv('datasets/cleaned/'+foldername+'/topics_'+foldername+'.csv')