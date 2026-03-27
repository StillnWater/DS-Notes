# Function to Sort a List using Bubble Sort Algorithm
def bubble_sort(lis: list):
    # Length of list
    n = len(lis)
    for i in range(n-1):
        for j in range(n-1-i):
            # Compare adjacent elements and swap if necessary
            if lis[j] > lis[j+1]:
                lis[j] , lis[j+1] = lis[j+1] , lis[j]

# Function to Sort a List using Selection Sort Algorithm
def selection_sort(lis: list):
    # Length of list
    n = len(lis)
    for i in range(n-1):
        ind = i
        for j in range(i+1,n):
            # Compare adjacent elements and update index if necessary
            if lis[ind] > lis[j]:
                ind = j
        lis[i] , lis[ind] = lis[ind] , lis[i]

# Function to Sort a List using Insertion Sort Algorithm
def insertion_sort(lis: list):
    # Length of list
    n = len(lis)
    for i in range(1, n):
        elem = lis[i]
        j = i-1
        while j >= 0 and elem < lis[j]:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = elem