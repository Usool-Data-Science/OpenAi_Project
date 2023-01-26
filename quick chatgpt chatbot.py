# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:53:58 2023

@author: user
"""

myApiKey = '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'
import openai
import os

os.environ['API_KEY'] = myApiKey

openai.api_key = os.environ['API_KEY']

def question():
    print('''Welcome to the AI chatbot to help you with your queries, I am here to respond to any question you ask, however please respect me by asking sensible questions. When you are done with your queries, please type done and enter key to exit.''')
    
    keep_prompting = True
    while keep_prompting:
        my_prompt = input('\n Please ask your question here >>: ')
        if my_prompt == 'done': 
            keep_prompting = False
        else: 
            result = openai.Completion.create(engine = 'text-davinci-003', # I can use 'text-curie-001' instead
                                              prompt = my_prompt, 
                                              max_tokens = 500)
            print('Your queries has',
                  result['usage']['total_tokens'],
                  'tokens and your result is as follow: \n' ,
                  result['choices'][0]['text'])
