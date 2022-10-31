import time
import os, psutil
import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("5_input.txt")
m = open("5_output.txt", "w")

string = f.readline()
numbers = list(map(int, string.split()))
numbers_new = quicksort(numbers)
m.write(str(numbers_new[int(len(numbers_new)/2)]))

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")