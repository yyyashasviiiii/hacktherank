"""
Problem: Loops
Link: https://www.hackerrank.com/challenges/python-loops/problem

Task:
Given an integer `n`, print the square of all non-negative integers less than `n`.
Each square should be printed on a new line.

Input Format:
- A single integer `n`.

Constraints:
- 1 <= n <= 20

Output Format:
Print `n` lines.
Each line should contain the square of a non-negative integer less than `n`.

Sample Input 0:
5

Sample Output 0:
0
1
4
9
16

Explanation:
The non-negative integers less than 5 are: 0, 1, 2, 3, 4.
Their squares are: 0²=0, 1²=1, 2²=4, 3²=9, 4²=16.
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i * i)