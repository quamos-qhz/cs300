import math
import random
def main():
    #print('hello')
    #print(linear_search([1,2,3,4,5,6],10))
    #print(binary_search([1,2,2,3,5],5))
    #print(binary_search([1, 2, 2, 3, 5],1))
    #print(binary_search([1, 2, 2,2,2,2, 3, 5], 2))
    #print(binary_search([1, 2, 2, 3, 5, 6], 4))
    #print(binary_search([1, 2, 2, 3, 5,6], 3))

    zeros = [0] * 100
    youtube = [17, 2, 12, 19, 21, 49, 20, 19]
    google = [0, 0, 0]
    num = []
    for i in range(1, 100):
        num.append(i)
    print(num)
    print(distinct(youtube))
    print(distinct(google))
    print(distinct(zeros))

    print(distinct(num))

    #print(distinct([1,2,3,4,5]))
    #print( math.floor((3+4)/2))


def linear_search(arr, x):



    """
    Performs linear search to find the index of `x` in `arr`.

    Parameters
    ----------
    arr : nonempty list of int
    x : int

    Returns
    -------
    int
        the index `i` such that `x == arr[i]` if such `i` exists,
        otherwise -1
    """

    length = len(arr)
    for i in range(length):
        if(arr[i] == x):
            return i
        i+=1
    return -1
    pass


def binary_search(arr, x):
    """
    Performs binary search on already sorted list to find the index for `x` in `arr`.

    Parameters
    ----------
    arr : nonempty list of int
        already sorted in ascending order
    x : int

    Returns
    -------
    int
        the smallest index `i` such that `x < arr[i]` while assuming that
        if `x` is greater than or equal to the largest element in `arr`,
        then return the length of `arr`
    """


    left = 0
    right = len(arr)-1
    most = arr[len(arr)-1]
    ans = 0
    if(x>=most):
        return len(arr)

    while(left < right):
        mid = math.floor((left+right)/2)

        if(x>=arr[mid]):
            left = mid + 1

        else:
            ans = mid
            right = mid

    return ans


    pass






def distinct(arr):
    '''
    Tests whether all elements in given list are distinct or not.
    (Please implement it using hashing as in lecture slides.)

    Parameters
    ----------
    arr : nonempty list of int
        whose length is at most 10,000 and whose elements are positive
    Returns
    -------
    bool
        `True` if all elements are distinct,
        `False` otherwise
    '''

    '''set1 = set(arr)
    lenS = len(set1)
    lenL = len(arr)
    if(lenL>lenS):
        return False
    return True'''

    if arr == (len(arr)) * [0]:
        return False

    ## we choose prime number as P = 10139
    y = [0] * 10138
    p = 42
    k = 17

    for i in range(len(arr)):
        p = (arr[i] * k) % 10139
        while y[p] != 0:
            if y[p] == arr[i]:
                return False
            p = (p + 1) % 10139
        y[p] = arr[i]
    return True


if __name__ == "__main__":
    main()
