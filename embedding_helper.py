import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
from openai import AzureOpenAI
import tiktoken 

#没有模块可使用pip下载： pip install XXX

#azure open ai的key和endpoint参数
API_KEY = "fced3f5d1b5a4b139d33537d44da6fbc"
RESOURCE_ENDPOINT = "https://open-ai-test-standard-01.openai.azure.com/" 

client = AzureOpenAI(
  api_key = API_KEY,  
  api_version = "2023-05-15",
  azure_endpoint = RESOURCE_ENDPOINT
)

#对于要转化矢量的参数可进行相应的数据处理
def normalize_text(s, sep_token = " \n "):
    s = re.sub(r'\s+',  ' ', s).strip()
    s = re.sub(r". ,","",s)
    # remove all instances of multiple spaces
    s = s.replace("..",".")
    s = s.replace(". .",".")
    s = s.replace("\n", " ")
    s = s.strip() 
    return s

#主要方法，调用azure embedding 模型
def generate_embeddings(text, model="azure_embedding_ada_model"): # model = "deployment_name"
    text = normalize_text(text)
    return client.embeddings.create(input = [text], model=model).data[0].embedding

# print(generate_embeddings('hello'))

#保存到文件中
def saveFile(content):
    try:
        file_path = "./static/hello01.txt"  #保存路径
        f = open(file_path, 'w+')
        print(f.write(str(content)))
    finally:
        if f:
            f.close()
#执行方法
texts = "How are embeddings generated? The open-source library called Sentence Transformers allows you to create state-of-the-art embeddings from images and text for free. This blog shows an example with this library"
emContent = generate_embeddings(texts)
saveFile(emContent)