"""
Problem: List Comprehensions
Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

Description:
You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid, and an integer `n`.

Your task is to print a list of all possible coordinates `[i, j, k]` on a 3D grid such that:
- 0 <= i <= x
- 0 <= j <= y
- 0 <= k <= z
- The sum (i + j + k) is not equal to `n`

The output list should be in lexicographic (ascending) order.

Input Format:
Four integers, one on each line:
- x
- y
- z
- n

Constraints:
- 0 <= x, y, z <= 100
- 0 <= n <= x + y + z

Output Format:
Print the list of coordinates where the sum is not equal to `n`, in lex order.

Sample Input 0:
1
1
1
2

Sample Output 0:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation:
All coordinates from (0,0,0) to (1,1,1) are generated.
The only coordinate where i + j + k == 2 is [0,1,1], [1,0,1], and [1,1,0], which are removed.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [
        [i,j,k] # expression
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n  # condition
    ]
    print(result)