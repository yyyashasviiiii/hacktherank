"""
Problem: Arithmetic Operators
Link: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

Task:
Given two integers, `a` and `b`, print the following three lines:

1. The sum of the two numbers (a + b)
2. The difference of the two numbers (a - b)
3. The product of the two numbers (a * b)

Input Format:
- The first line contains the integer `a`.
- The second line contains the integer `b`.

Constraints:
1 <= a <= 10^10  
1 <= b <= 10^10

Output Format:
Print the following three results, each on a new line:
- The sum (a + b)
- The difference (a - b)
- The product (a * b)

Sample Input 0:
3
2

Sample Output 0:
5
1
6

Explanation:
- Sum: 3 + 2 = 5
- Difference: 3 - 2 = 1
- Product: 3 * 2 = 6
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a + b)
    print(a - b)
    print(a * b)