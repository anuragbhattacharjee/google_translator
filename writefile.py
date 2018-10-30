from readfile import readfile
import os

def writefile(address, wordList = []):
    address = './dict/' + address
    # existingWords = readfile(address)
    if not os.path.exists(address):
        os.makedirs(address) 
    with open(address + '/intent.txt', 'a') as out:
        for word in wordList:
            # if word not in existingWords:
            out.write('\n' + word + '\n')

    out.close()