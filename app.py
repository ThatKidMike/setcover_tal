from itertools import chain, combinations, permutations, product
import time
from random import random, randrange

def powerset(iterable):
    universe = list(iterable)
    return chain.from_iterable(combinations(universe, r) for r in range(1, len(universe) + 1))

def subsets(iterable):
    universe = list(iterable)
    subsets = filter(lambda sub: len(sub) <= 2, universe)
    return subsets

#def exact_algorithm(subsets, universe):
  #  subsets = list(subsets)
  #  universe = list(universe)
   # permutated = chain([list(subsets) for subsets in permutations(subsets, n)] for n in range(1, len(universe)+1))
   # unwrappedPermutated = list(chain.from_iterable(permutated))
   # minLen = len(universe)
   # minInnerElements = len(universe)
   # print(unwrappedPermutated)
   # finalSubset = []
    #for elem in unwrappedPermutated:
     #   if set(chain.from_iterable(elem)).issuperset(set(universe)):
     #       if len(elem) <= minLen:
      #          if len(list(chain.from_iterable(elem))) <= minInnerElements:
      #              finalSubset = elem
      #              minLen = len(elem)
    #return finalSubset

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

def subsets_gen(iterable):
    wholeSubsets = []
    iterator = 0
    tempSet = set()
    while iterator != len(iterable):
        for i in range (0,4):
            if iterator >= len(iterable):
                break
            tempSet.add(iterable[iterator])
            iterator += 1
        wholeSubsets.append(tempSet)
        tempSet = set()
    tempSubset = set()   
    madeSubset = set()
    for i in range(0, 5000000):
        endrange = randrange(0,7)
        for j in range(1, endrange):
            while len(madeSubset) < endrange:
                index = randrange(0,len(iterable))
                madeSubset.add(iterable[index])
        if len(madeSubset) > 0:
            wholeSubsets.append(madeSubset)
        madeSubset = set()
    return wholeSubsets


initialSet = []
for i in range(1,150):
    initialSet.append(i)
subs = subsets_gen(initialSet)
subs2 = subs.copy()
print("MEASURE TIME!")
print('######################################')
#print(list(subs))
#pows = powerset(initialSet)
#subs = subsets(pows)

exactSummator = 0
greedySummator = 0

for i in range (0, 20):
    start1 = time.time()
    results_exact = exact_algorithm_reforged(subs, initialSet)
    print(results_exact)
    print(len(list(chain.from_iterable(list(results_exact)))))
    end1 = time.time()
    exactSummator += float(end1 - start1)


print('#######################################')

for i in range (0, 20):
    start1 = time.time()
    results_greedy = greedy_algorithm(subs, initialSet)
    print(results_greedy)
    print(len(list(chain.from_iterable(list(results_greedy)))))
    end1 = time.time()
    greedySummator += float(end1 - start1)


print(float(exactSummator)/20)
print(float(greedySummator)/20)



