"""
Problem: Text Alignment (HackerRank Logo)
Link: https://www.hackerrank.com/challenges/text-alignment/problem

Description:
You are given an odd integer `thickness`, which controls the size of the HackerRank 'H' logo.
Using Python’s built-in string alignment methods (`ljust()`, `rjust()`, and `center()`), your task is to print the stylized logo made entirely of the letter 'H'.

The logo consists of 5 parts:
1. Top Cone      - An expanding triangle at the top center
2. Top Pillars   - Two tall vertical pillars
3. Middle Belt   - A wide horizontal bar joining both pillars
4. Bottom Pillars- Repeats the Top Pillars
5. Bottom Cone   - An inverted triangle aligned to the right

Input Format:
- A single odd integer: `thickness`

Constraints:
- 1 <= thickness <= 50
- `thickness` must be an odd number (guaranteed by the problem)

Output Format:
- A stylized ASCII art 'H' logo, aligned using string formatting functions.

Sample Input 0:
5

Sample Output 0:
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                        HHHHHHHHH 
                         HHHHHHH  
                          HHHHH   
                           HHH    
                            H      

Explanation:
- Each section of the logo is generated using loops and alignment methods.
- Alignment logic is based on the `thickness`, ensuring proper spacing and structure.

"""

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness + 1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness - i - 1)).rjust(thickness) + c + (c*(thickness - i - 1)).ljust(thickness)).rjust(thickness*6))