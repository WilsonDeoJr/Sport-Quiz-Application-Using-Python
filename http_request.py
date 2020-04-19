import requests
import json
import pprint
import random as rd
from tkinter import *


Error = ''
try:
    status = requests.get('https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple')
    status.raise_for_status()
    statuscode = status.status_code
    index = rd.randint(0,9)  
    data = json.loads(status.text)

    def questioners():
        questions = data['results'][index]['question']
        return questions

    def choices(index_num):
        incorrect = data['results'][index]['incorrect_answers']
        correct = data['results'][index]['correct_answer']
        answers_bank = [incorrect[0],incorrect[1],incorrect[2], correct]
        
        return answers_bank[index_num]

    
except requests.exceptions.HTTPError as err:
    Error = SystemExit(err)
    raise Error






    
    
    
 
        

    

