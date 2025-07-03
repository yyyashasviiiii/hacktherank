"""
Problem: Set .add() – Distinct Country Stamps
Link: https://www.hackerrank.com/challenges/py-set-add/problem

Description:
Rupal has a large collection of country stamps. Your task is to help her count the number of **distinct** country stamps.
You are given a sequence of country names (stamps) and must determine how many unique countries are in the collection.

You should use a `set` to store and automatically filter out duplicates using the `.add()` operation.

Function Signature:
def count_unique_stamps(n: int, countries: List[str]) -> int

Parameters:
- n (int): The total number of country stamps.
- countries (List[str]): A list of country names, one per stamp.

Returns:
- int: The number of distinct countries in the collection.

Input Format:
- The first line contains the integer `n`, the number of stamps.
- The next `n` lines each contain a country name (string).

Output Format:
- Output a single integer, the number of unique country names.

Constraints:
- 0 < n ≤ 1000
- Each country name is a non-empty string containing alphabetic characters and spaces.

Sample Input:
7
UK
China
USA
France
New Zealand
UK
France

Sample Output:
5

Explanation:
There are 7 country stamps in total, but some are duplicates.
The distinct country names are: UK, China, USA, France, New Zealand — 5 in total.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set()
for i in range(n):
    s.add(input())

print(len(s))