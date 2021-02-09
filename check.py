#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Description: This is a chatbot project 


# In[2]:





# In[3]:




# In[4]:


#import libraries 
from newspaper import Article
import random
import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[5]:


#Download punkt package
nltk.download('punkt', quiet=True)


# In[6]:


#Get article 
article = Article('https://www.python.org/doc/essays/blurb/')
article.download()
article.parse()
article.nlp()
corpus = article.text


# In[8]:


#Print the article data
print(corpus)


# In[9]:


#Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)
#List of sentences 


# In[10]:


#Function to return greeting response 
def greeting_response(text):
    text = text.lower()
    
    #Bots greeting response 
    bot_greetings = ['hello', 'hi', 'hola', 'namaste', 'hey']
    #Users greetings 
    user_greetings = ['hey', 'hi', 'hello', 'hola', 'namaste', 'sup']
    
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


# In[11]:


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                
    return list_index


# In[12]:


#Create the bot response 
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0 
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            respone_flag = 1 
            j = j+1
        if j > 2:
            break
            
    if response_flag == 0:
        bot_response = bot_response+' '+"I don't understand you, apologies."
        
    sentence_list.remove(user_input)
    
    return bot_response 


# In[ ]:


### Start the chat
print('I am candybot and i will talk to you. To end the chat, type goodbye.')

end_list = ['exit', ' bye', 'see you soon', 'quit']

while(True):
    user_input = input()
    if user_input.lower() in end_list:
        print('candybot: talk to you soon, have a good day')
        break
        
    else: 
        if greeting_response(user_input) != None:
            print('candybot: '+greeting_response(user_input))
        else:
            print('candybot: '+bot_response(user_input))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




