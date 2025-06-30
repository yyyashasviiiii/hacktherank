"""
Problem: Print Function
Link: https://www.hackerrank.com/challenges/python-print/problem

Description:
Given an integer `n`, print all integers from 1 to `n` in a single line, without using any string methods or spaces.
Each number should appear directly next to the previous one (i.e., no separator).

Note:
- Do not use string conversion functions like `str()`, `join()`, or string concatenation.
- Use only basic print logic, such as a loop with `print(i, end='')`.

Input Format:
- A single integer `n`.

Constraints:
1 <= n <= 150

Output Format:
- Print the numbers from 1 to `n` (inclusive) in one line with no space or separator.

Sample Input 0:
3

Sample Output 0:
123

Explanation:
The integers from 1 to 3 are printed in sequence without spaces.
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i, end="")