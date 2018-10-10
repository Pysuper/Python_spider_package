# 选择排序
a = [49, 38, 65, 97, 76, 13, 27, 49]
for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j
    # a[i],a[m] = a[m],a[i]
    temp = a[i]
    a[i] = a[m]
    a[m] = temp
# print(a)

# 冒泡排序
a = [77,42,35,12,101,5]
for i in range(len(a)-1):
    flag = True
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

            flag = False
    if flag == True:
        break
# print(a)

#　定义函数排序
import math

def IsPrime(a):
    m = int(math.sqrt(a))
    for i in range(2,m+1):
        if a%i == 0:
            return False
    return True

for i in range(2,200):
    if IsPrime(i) == True:
        pass
        # print(i)

# 函数封装冒泡排序
def Bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
a = [77,42,35,12,101,5]
Bubble_sort(a)
# print(a)

# 递归函数--求ｎ的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        return s

i = factorial(10)
# print(i)

# 归并排序
def merge(left,right):
    pass


def shell(arr):
    n = len(arr)
    h = 1
    while h < n / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
                h = h // 3
    print(arr)

q=[1,4,23,42,424,242,4]
# shell(q)


