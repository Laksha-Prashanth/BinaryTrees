import random

def getRandomArray():
    result = [i for i in range(10000)]
    random.shuffle(result)
    return result
