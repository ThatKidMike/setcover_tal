from itertools import chain, combinations, permutations, product
import time
from random import random, randrange


def exact_algorithm_reforged(sub, univer):
    subsets = list(sub)
    subsets = sorted(subsets, key=len, reverse=True)
    smallUniverse = list(univer)
    finalSubset = []
    currPsbIntersec = 0
    currElem = subsets[0]
    finalSubset.append(currElem)
    smallUniverse = set(smallUniverse) - set(currElem)
    while len(list(smallUniverse)) != 0:
        for elem in subsets:
            if len(set(elem).intersection(chain.from_iterable(list(finalSubset)))) == currPsbIntersec:
                smallUniverse = set(smallUniverse) - set(elem)
                finalSubset.append(elem)
            if len(list(smallUniverse)) == 0:
                break 
        currPsbIntersec+=1
    return finalSubset

def exact_algorithm_remake(sub, univer):
    for iter in range(1, len(univer)+1):
        for comb in combinations(sub, iter):
            if len(list(univer)) == len(list((chain.from_iterable(list(comb))))):
                if list(univer) == list((chain.from_iterable(list(comb)))):
                    return(comb)

def greedy_algorithm(sub, univer):
    universe = list(univer)
    subsets = list(sub)
    subsets = sorted(subsets, key=len, reverse=True)
    finalSubset = []
    currElem = subsets[0]
    finalSubset.append(currElem)
    smallUniverse = universe
    smallUniverse = set(smallUniverse) - set(currElem)
    iterator = 0
    while len(list(smallUniverse)) != 0:
        for elem in subsets:
            if len(set(elem).intersection(set(smallUniverse))) >= 1:
                finalSubset.append(elem)
                smallUniverse = set(smallUniverse) - set(elem)
            if len(list(smallUniverse)) == 0:
                break
    return finalSubset

def subsets_gen(iterable, subsetsAmt):
    wholeSubsets = []
    iterator = 0
    tempSet = set()
    while iterator != len(iterable):
        for i in range (0,2):
            if iterator >= len(iterable):
                break
            tempSet.add(iterable[iterator])
            iterator += 1
        wholeSubsets.append(tempSet)
        tempSet = set()
    tempSubset = set()   
    madeSubset = set()
    tempSet = set()
    for i in range(1, 2):
        tempSet.add(i)
    wholeSubsets.append(tempSet)
    tempSet = set()
    for i in range(2, 4):
        tempSet.add(i)
    wholeSubsets.append(tempSet)
    tempSet = set()
    for i in range(4, 8):
        tempSet.add(i)
    wholeSubsets.append(tempSet)
    tempSet = set()
    for i in range(8, 10):
        tempSet.add(i)
    wholeSubsets.append(tempSet)
    tempSet = set()
    for i in range(0, int(subsetsAmt)):
        endrange = randrange(0,3)
        for j in range(1, endrange):
            while len(madeSubset) < endrange:
                index = randrange(0,len(iterable))
                madeSubset.add(iterable[index])
        if len(madeSubset) > 0:
            wholeSubsets.append(madeSubset)
        madeSubset = set()
    return wholeSubsets


rangeStart = input("Universe start: ")
rangeEnd = input("Universe stop: ")
compareLoop = input("How many times loop through the algorithms: ")
subsetsAmt = input("How many subsets to generate: ")


initialSet = []
for i in range(int(rangeStart), int(rangeEnd)):
    initialSet.append(i)
subs = subsets_gen(initialSet, int(subsetsAmt))
subs2 = subs.copy()
print("MEASURE TIME!")
print('######################################')

exactSummator = 0
greedySummator = 0

for i in range (0, int(compareLoop)):
    start1 = time.time()
    results_exact = exact_algorithm_remake(subs, initialSet)
    print(results_exact)
    print(len(list(chain.from_iterable(list(results_exact)))))
    end1 = time.time()
    exactSummator += float(end1 - start1)

print('#######################################')

for i in range (0, int(compareLoop)):
    start1 = time.time()
    results_greedy = greedy_algorithm(subs, initialSet)
    print(results_greedy)
    print(len(list(chain.from_iterable(list(results_greedy)))))
    end1 = time.time()
    greedySummator += float(end1 - start1)

print(float(exactSummator)/1)
print(float(greedySummator)/1)




