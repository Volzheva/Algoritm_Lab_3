import time
import os, psutil
import random


def quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("6_input.txt")
m = open("6_output.txt", "w")

string1 = f.readline()
string2 = f.readline()
string3 = f.readline()
numbers_1 = list(map(int, string2.split()))
numbers_2 = list(map(int, string3.split()))
numbers = []
for i in numbers_1:
    for j in numbers_2:
        numbers.append(i*j)
quicksort(numbers, 0, len(numbers) - 1)
numbers_good = []
a = len(numbers)//10
b = 0

for i in range(0, a+1):
    numbers_good.append(numbers[i*10])


m.write(str(sum(numbers_good)))
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")