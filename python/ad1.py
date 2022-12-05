import numpy as np

with open('input1.txt') as f:
    input = f.read()
    
calorie_sums = [sum(map(int,[y for y in x.strip().split('\n')])) for x in input.split('\n\n')] #Parse list and convert to int, then sum
max_index = np.argmax(calorie_sums)
print(max_index, calorie_sums[max_index])
