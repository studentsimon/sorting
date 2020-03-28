#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    new1 = []
    lengthxs = len(xs)
    lengthys = len(ys)
    x = 0
    y = 0

    while x < lengthxs and y < lengthys:
        if ((cmp == cmp_standard and xs[x] >= ys[y]) or (cmp == cmp_reverse and xs[x] <= ys[y])):
            new1.append(ys[y])
            y = y + 1
        elif ((cmp == cmp_standard and xs[x] < ys[y]) or (cmp == cmp_reverse and xs[x] > ys[y])):
            new1.append(xs[x])
            x = x + 1

    if x == lengthxs and y == lengthys: #assumes full completion
              return new1 
    elif x == lengthxs and y != lengthys:
        for z in range (y, lengthys):
            new1.append(ys[z])
        return new1
    elif y == lengthys:
        for z in range (x, lengthxs):
            new1.append(xs[z])
        return new1

def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs)//2
        l = xs[:mid]
        r = xs[mid:]
        merge_sorted(l, cmp=cmp) #sort left
        merge_sorted(r, cmp=cmp) #sort the right
        return _merged(merge_sorted(l,cmp=cmp), merge_sorted(r, cmp=cmp), cmp=cmp) #merge the two sorted halves
    
    


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    hi = []
    lo = []
    pi = []

    
    if len(xs) <= 1: #as stated
        return xs
    else:
        x = xs[0]
        for z in xs:
            if z > x:
                hi.append(z)
            elif z < x:
                lo.append(z)
            else:
                pi.append(z)
        less = quick_sorted(lo, cmp=cmp)
        greater = quick_sorted(high,cmp=cmp)

        if cmp == cmp_standard:
            return less + pi + greater #return the concatenation of (less than, p, and greater than)
        if cmp == cmp_reverse:
            return greater + pivot + less #return the concatenation of (less than, p, and greater than)

    

def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''

