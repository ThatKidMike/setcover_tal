from itertools import chain, combinations, permutations, product
import time
from random import random, randrange, shuffle


def exact_algorithm_remake(sub, univer):
    for iter in range(0, len(sub)):
        for comb in combinations(sub, iter):
            if len(list(univer)) == len(list((chain.from_iterable(list(comb))))):
                if set(univer) == set((chain.from_iterable(list(comb)))):
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

def subsets_gen(iterable, subsetsAmt, maxSubsetRange):
    wholeSubsets = []
    iterator = 0
    setIterator = 0
    tempSet = set()
    madeSubset = set()
    iterableCopy = iterable.copy()
    shuffle(iterableCopy)
    while len(iterableCopy) != 0:
        randSubsetRange = randrange(1, maxSubsetRange+1)
        while randSubsetRange > len(iterableCopy):
            randSubsetRange = randrange(1, maxSubsetRange+1)
        for i in range(0, randSubsetRange):
            tempSet.add(iterableCopy.pop(0))
        wholeSubsets.append(tempSet)
        setIterator += 1
        tempSet = set()
    while setIterator != subsetsAmt:
        endrange = randrange(1, maxSubsetRange+1)
        for j in range(1, endrange):
            while len(madeSubset) < endrange:
                index = randrange(0, len(iterable)-1)
                madeSubset.add(iterable[index])
        if len(madeSubset) > 0:
            wholeSubsets.append(madeSubset)
            setIterator += 1
        madeSubset = set()
    shuffle(wholeSubsets)
    return wholeSubsets


rangeStart = input("Universe start: ")
rangeEnd = input("Universe stop: ")
compareLoop = input("How many times loop through the algorithms: ")
subsetsAmt = input("How many subsets to generate: ")
maxRange = input("Max range of subsets: ")


initialSet = []
for i in range(int(rangeStart), int(rangeEnd)+1):
    initialSet.append(i)
subs = subsets_gen(initialSet, int(subsetsAmt), int(maxRange))
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

print(float(exactSummator)/int(compareLoop))
print(float(greedySummator)/int(compareLoop))