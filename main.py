import eland as ed
from elasticsearch import Elasticsearch
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings()

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.getenv('ELASTIC_PASSWORD')),
    verify_certs=False
)

df = ed.DataFrame(es, es_index_pattern="heart-rates")

pandas_df = ed.eland_to_pandas(df)

pandas_df['thal'] = pd.Categorical(pandas_df['thal'])
pandas_df['thal'] = pandas_df.thal.cat.codes

target = pandas_df.pop('target')

dataset = tf.data.Dataset.from_tensor_slices((pandas_df.values, target.values))

for feat, targ in dataset.take(5):
  print ('Features: {}, Target: {}'.format(feat, targ))

tf.constant(pandas_df['thal'])

train_dataset = dataset.shuffle(len(pandas_df)).batch(1)

def get_compiled_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
  ])

  model.compile(optimizer='adam',
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=['accuracy'])
  return model

model = get_compiled_model()
model.fit(train_dataset, epochs=15)