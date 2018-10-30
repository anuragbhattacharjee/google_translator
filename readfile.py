import os

def readfile(address): 
    lines = [] 
    with open('./dict/' + address ,'r') as f:
        lines = f.read().splitlines()

    f.close()
    return lines