import json

import numpy as np

with open("../data/sampleJson.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)

var = '01234567'
print(var[::2])

# cast float to int
x = 1.9
print(int(x))  # 1

print("------ -------".split())


def add(x): return (x + x)


print(add('1'))
a = np.array([0, 1, 0, 1, 0])
b = np.array([1, 0, 1, 0, 1])
#print(a / b)

a = np.array([1, 1, 1, 1, 1])
print(a + 10)
