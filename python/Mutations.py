"""
Problem: Mutations
Link: https://www.hackerrank.com/challenges/python-mutations/problem

Description:
Strings in Python are immutable, meaning they cannot be changed directly by index assignment.
To modify a character at a specific position in a string, we can:
- Convert the string to a list, modify the list, and join it back into a string.
- Or use slicing to construct a new string with the desired modification.

Task:
Given a string, an index position, and a character, return a new string where the character at the given index is replaced with the provided character.

Function Signature:
def mutate_string(string: str, position: int, character: str) -> str

Parameters:
- string (str): The original string.
- position (int): The index at which to modify the character.
- character (str): The new character to insert at the specified position.

Returns:
- str: The modified string with the character replaced at the given index.

Input Format:
- The first line contains the original string.
- The second line contains the position (as an integer) and the character (as a single character), separated by a space.

Output Format:
- Return the modified string.

Sample Input:
abracadabra
5 k

Sample Output:
abrackdabra

Example:
>>> mutate_string("abracadabra", 5, "k")
'abrackdabra'
"""

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)