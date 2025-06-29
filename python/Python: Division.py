"""
Problem: Python: Division
Link: https://www.hackerrank.com/challenges/python-division/problem

Task:
Given two integers `a` and `b`, perform the following operations:

1. Print the result of integer division (a // b)
2. Print the result of float division (a / b)

Note:
- Do not round or format the results.
- Integer division (//) returns the quotient without the decimal part.
- Float division (/) returns the precise result including decimals.

Input Format:
- The first line contains the integer `a`.
- The second line contains the integer `b`.

Constraints:
- 1 <= a <= 10^10
- 1 <= b <= 10^10

Output Format:
Print the result of:
1. Integer division (a // b)
2. Float division (a / b)

Sample Input 0:
4
3

Sample Output 0:
1
1.3333333333333333

Explanation:
- Integer division of 4 by 3 yields 1.
- Float division of 4 by 3 yields 1.3333333333333333.
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a // b)
    print( a / b)