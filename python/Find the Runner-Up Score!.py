"""
Problem: Runner-Up Score
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Description:
Given the scores of participants in a competition, find and print the **runner-up score** — the second highest score in the list (distinct from the highest).

The runner-up score is defined as the highest score in the list that is **strictly less** than the maximum score.

Input Format:
- The first line contains an integer `n`, the number of scores.
- The second line contains `n` space-separated integers representing the scores.

Constraints:
- 2 <= n <= 10
- -100 <= score <= 100

Output Format:
- Print the runner-up score (an integer) on a single line.

Sample Input 0:
5
2 3 6 6 5

Sample Output 0:
5

Explanation:
- The highest score is 6, which occurs twice.
- The next highest distinct score is 5, so the runner-up is 5.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    
    print(arr[-2])