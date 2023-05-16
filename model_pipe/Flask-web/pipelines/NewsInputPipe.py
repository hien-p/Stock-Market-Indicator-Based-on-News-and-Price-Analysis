import pandas as pd
import os
import sys
# from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
import joblib
import numpy as np
import tensorflow as tf

def read_csv(data_path):
    df = pd.read_csv(data_path)
    return df

def lower_x_col(df, x_col):
    df[x_col] = df[x_col].apply(lambda y: y.lower())
    return df

def shift_y_col(df, y_col, label_off):
    df[y_col] -= label_off
    return df

def download_tokenizer(bert_version):
    tokenizer = BertTokenizer.from_pretrained(bert_version)
    return tokenizer

def load_tokenizer(path):
    tokenizer = joblib.load(path)
    return tokenizer

### train_test_split_methods ###
class Spliter:  

    def split_3sets(df, test_size, validate_size):
        Train, test = train_test_split(df, test_size = test_size)
        train, vali = train_test_split(Train, test_size = validate_size)
        return [train, vali, test]

class InputPipeline:

    def DatasetMapFunction(input_ids, attn_masks, labels):
        #this function used for fomatting the input to BERT
        return {
            'input_ids':input_ids,
            'attention_mask':attn_masks
        },labels

    
    def one_hot_encode(df):
        num_labels = len(df.unique())
        y_label = np.zeros((len(df),num_labels))
        y_label[np.arange(len(df)), df.values] = 1
        return y_label

    def tokenize_news(data, tokenizer, token_len):
        ids = np.zeros((len(data),token_len))
        masks = np.zeros((len(data),token_len))
        for i, text in enumerate(data):
            tokenized_text = tokenizer.encode_plus(\
                text, max_length=token_len, truncation=True,\
                padding='max_length', add_special_tokens=True,\
                return_tensors='tf')
            ids[i,:] = tokenized_text.input_ids
            masks[i,:] = tokenized_text.attention_mask
        return ids, masks

    
    def wrap_tf_dataset(input_ids, attn_msk, labels, batch=10, shuffle=False):
        dataset = tf.data.Dataset.from_tensor_slices((input_ids, attn_msk, labels))
        dataset = dataset.map(InputPipeline.DatasetMapFunction\
            ,num_parallel_calls=tf.data.AUTOTUNE)
        
        if shuffle:
            d_size = labels.shape[0]
            text_ds = dataset.shuffle(d_size).batch(batch)
        else:
            text_ds = dataset.batch(batch)
        text_ds = text_ds.cache()
        text_ds = text_ds.prefetch(tf.data.AUTOTUNE)
        return text_ds

### run_methods: the below functions are data preparation pipeline ###

def prepare_model_tf_input(data_path, x_col, y_col, bert_version='bert-base-multilingual-cased'\
        ,token_len = 256, label_off=1, batch=10, shuffle=False):
    df = read_csv(data_path)
    df = lower_x_col(df, x_col)
    df = shift_y_col(df, y_col, label_off)
    tokenizer = load_tokenizer(f'./tokenizers/{bert_version}-tokenizer.pkl')
    i_ids, a_msk = InputPipeline.tokenize_news(df[x_col], tokenizer, token_len)
    hot_label = InputPipeline.one_hot_encode(df[y_col])
    ds = InputPipeline.wrap_tf_dataset(i_ids, a_msk, hot_label, batch, shuffle)
    print("Data is served")
    return ds
