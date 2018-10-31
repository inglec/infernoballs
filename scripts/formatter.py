# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re


def formatSha512(potfile,hashfile):
    count=0
    x = []
    y = []
    z = []
    with open("..\\infernoballs\\broken\\sha512.broken") as file1:
        for l in file1:
            x.append(l.strip())
            #print(x)
    with open("infernoball1.hashes") as file2:
        for l in file2:
            y.append(l.strip())
            #print(y)
    
    for hashes in x:
        aPswdHash = hashes.split(':')[0]
        escPswdHash = re.escape(aPswdHash.split('$')[4])
        #print('hash is ----->',escPswdHash)
        for shr in y:
            #print(shr)
            escShrHash = re.escape((shr.split(':')[1]).split('$')[4])
            #print(escShrHash) 
            #if(re.match(escPswdHash,escShrHash)):
            if(escShrHash.find(escPswdHash)!=-1):
                #print(True)
                count += 1
                #print(count)
                z.append(shr.split(':')[0]+':'+hashes.split(':')[1])#.append(':').append(hashes.split(':')[1])
                break
                
                
    print (count)
    print(z)
    return z


def main():
    potfile = 1
    hashfile =2
    matchArr = formatSha512(potfile,hashfile)
    with open('sha512_.broken', 'w') as f:
        for item in matchArr:
            f.write("%s\n" % item)
    

if __name__== "__main__":
    main()
    