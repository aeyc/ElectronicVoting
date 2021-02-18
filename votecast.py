#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 02:40:36 2020

@author: Ayca
"""
import random
import numpy as np


VOTING_SESSION = 10


#randomBinaryGenerator method 
#to produce randomly generated l-length binary string
#param:l length of the binary string
#returns:b as the random binary string with the given length
def randomBinaryGenerator(l):
    b = ""
    for i in range(l):
        b += str(random.randint(0,1))
    return b

if __name__ == "__main__":
    n = 4 #number of options offered to voters
    w_u = randomBinaryGenerator(n) #upper string
    w_l = randomBinaryGenerator(n) #lower string 
    w_u = "0010" #upper string
    w_l = "0111" #lower string 
    
    q = randomBinaryGenerator(VOTING_SESSION) #unique serial number
    
    ballot = []
    for i in range(n):
        option = [[w_u[i],w_l[i]],[w_u[i],w_l[i]]]
        ballot.append(option)
    print("Initial:",ballot)
    vote = int(input("Vote:")) #take vote
    
    information_bits = ((0,1),(1,0))
    #invert selection
    if (ballot[vote][0][1] =="0"): ballot[vote][0][1] ="1"
    elif(ballot[vote][0][1] =="1"): ballot[vote][0][1] ="0"
    if (ballot[vote][1][0] =="0"): ballot[vote][1][0] ="1"
    elif(ballot[vote][1][0] =="1"): ballot[vote][1][0] ="0"
    
    #encryption
    for i in range(len(ballot)):
        for j in range(len(ballot[0])):
            for k in range(len(ballot[0][0])):
                if ballot[i][j][k]== "0": ballot[i][j][k] ='♥'
                else: ballot[i][j][k] = '♠'
                
    epsilon_u = (vote,information_bits)
    epsilon_l = (vote,information_bits)
    
    toBePrinted = []
    for i in range(len(ballot)):
        for j in range(len(ballot[0])):
            if j==0:
                toBePrinted.append(ballot[i][j])
                
    print(ballot,"\n")
    print(toBePrinted)

    #decryption
    decrypted = toBePrinted+toBePrinted
    decrypted = np.array(decrypted)
    decrypted = decrypted.reshape((2,int(len(decrypted)))) #rearrenge ballot
    #but we need altering due to voting
    
    #guess this should be after shuffle
    loc = (epsilon_l[0]*2,epsilon_l[0]*2+1)
    if (decrypted[1][loc[0]] =='♥'): decrypted[1][loc[0]] ='♠'
    elif(decrypted[1][loc[0]] =='♠'): decrypted[1][loc[0]] ='♥'
    if (decrypted[1][loc[1]] =='♥'): decrypted[1][loc[1]] ='♠'
    elif(decrypted[1][loc[1]] =='♠'): decrypted[1][loc[1]] ='♥'

    
                
                