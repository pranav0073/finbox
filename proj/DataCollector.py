#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:53:01 2019

@author: pprashan
"""

from collections import Counter
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
s = "hello there whats up"
path = dir_path + "/finefoods.txt"
error = 0
num = 1



class Review:
    def __init__(self,data):
        self.pid = data['productId']
        self.uid = data['userId']
        self.profileName = data['profileName']
        self.helpfulness = data['helpfulness']
        self.score = float(data['score'])
        self.time = data['time']
        self.summary = data['summary']
        self.txt = data['text']
        self.factor = 0
        self.matching_words = []
    def getReviewTokens(self):
        text = set(map(lambda x: x.lower() ,self.txt.split()))
        return text
        
    def __str__(self):
        return str(("review/product: ", self.pid, "factor :",self.factor, 
                    "summary :", self.summary,"score :",self.score, 
                    "text :", self.txt))
       
    def __eq__(self,x):
        return self.score == x.score
    
    def __lt__(self,x):
        
        if self.factor == x.factor:
            return not self.score <= x.score
        
        return not self.factor < x.factor


    def add_factor(self,x):
        self.factor = x
    
 
 

def getReviews(queryString):       
    q_list =  set(queryString.split())
    count = 0
    attrCounter =  0
    prod = 0
    rlist = list()
    with open(path) as f:
        tempData = {}
        for line in f:
            
            
            
            if(line.strip() != "" ):
                
                attrCounter = (attrCounter) % 8 + 1
                
            
                    
                if(attrCounter != 0):
                    
                    z = line.split(": ")[0].split('/')[1]
                    tempData[str(z[:len(z)])] = line.split(": ")[1].replace('\n','')
                    
                if(attrCounter == 8):
                    prod += 1
                    #print(tempData)
                    rlist.append(Review(tempData))
                    tempData.clear()
                    
                    
                
                    
                
                    
                
                    #insert item in the list
                
                
            if(prod == 75000):
                
                break
        
        


    print(len(rlist))
    count = 0
    Rrlist = list()
    for review in rlist:
        
        
        result  = set(q_list.intersection(review.getReviewTokens()))
    
        review.factor = len(result)
        review.matching_words = result
        if len(result) > 0:
            
            Rrlist.append(review)
            count += 1

    Rrlist.sort()
    
    return Rrlist
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
