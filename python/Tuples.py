"""
Problem: Tuple Hash
Link: https://www.hackerrank.com/challenges/python-tuples/problem

Description:
Given an integer n and a line of space-separated integers, create a tuple from the integers,
and compute its hash using Python's built-in `hash()` function.

Input:
- First line: An integer n (number of elements)
- Second line: n space-separated integers

Output:
- A single integer — the hash of the tuple

Example:
Input:
2
1 2

Output:
3713081631934410656
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)

print(hash(t))

# for me my code wasn't working on Python3
# Due to how hash works and generate different results on machines

# n = int(input())
# t = tuple(map(int, input().split()))
# print(hash(t))