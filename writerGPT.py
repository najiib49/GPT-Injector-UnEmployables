# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 03:34:15 2023

@author: adila
"""

import openai
def paragraph(title):
    def open_file(path): #opens apikey
        with open(path,'r', encoding='utf-8') as infile:
            return infile.read()
    openai.api_key = open_file('ApiKey.txt')
    
    prompt = 'Write a 1000 word sarcastic negative paragraph about the '+title+' website'
    
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)
    
    txt = response["choices"][0]["text"]
    return txt