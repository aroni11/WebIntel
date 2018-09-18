import hashlib
import string
import random

def cleanUpString(inputStr):
    table = str.maketrans('', '', string.punctuation)
    return inputStr.translate(table).lower()


def compare(shinglesA, shinglesB):
    hashSetA = []
    hashSetB = []
    for subSet in shinglesA:
        hashSetA.append(hashFuncOne(' '.join(subSet)))

    for subSet in shinglesB:
        hashSetB.append(hashFuncOne(' '.join(subSet)))

    union = set()
    union.update(hashSetA, hashSetB)
    setHashSetA = set(hashSetA)
    setHashSetB = set(hashSetB)
    overlap = setHashSetA.intersection(setHashSetB)
    print(hashSetA)
    return len(overlap) / len(union)


def createSet(string):
    words = string.split(' ')
    wordSet = []
    numWords = len(words)-1 # 10

    for i in range(0, numWords): # i = starting index
        if i+2 <= numWords:
            wordSet.append([words[i], words[i+1], words[i+2]])
    return wordSet


def hashFuncOne(inputString):
    return hashlib.md5(inputString.encode()).hexdigest()

#MinHash Algorithm -> h(x) = (a'x + b') % c
#a' and b' are randomly chosen integers less than the maximum value of x.
#c is a prime number slightly bigger than the maximum value of c

#MinHash application
def applyMinHash(i, maxID):

    #Random list of generated integers
    randomList = []

    #Populte the list with different random indexes
    while i > 0:
        index = random.randint(0, maxID)

        #Prevent duplicates
        while index in randomList:
            index = random.randint(0, maxID)

        randomList.append(index)
        i -= 1

    return randomList

