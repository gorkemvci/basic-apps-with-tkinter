import requests
import random


class Question:
    def __init__(self): 
        self.counter = 0         
        self.param_list ={
                    "amount": 10 ,
                    "type" : "boolean"
                    }
        self.response = requests.get(url="https://opentdb.com/api.php", params= self.param_list) 
        self.response.raise_for_status()
        self.data =self.response.json()
        _myvar = 5
        Myvar = 10
        my-var =10


      
    


    



