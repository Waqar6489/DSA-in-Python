# recursion problem
# [1,1,2,3,5,8,13,21.....] sum previous two number
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        # previous 1 + previous 2
        return fibo(n-1) + fibo(n-2) # work like if agrument pass 5 then start 1, 1, 2, 3,5,8
    
print(fibo(5)) 

"""
fibo(1) → 1   
fibo(2) → 1
fibo(3) → 2 (1 + 1) # previous sum two
fibo(4) → 3 (1 + 2)
fibo(5) → 5 (2 + 3)
fibo(6) → 8 (3 + 5)
"""

"""               fibo(5)
                /         \
          fibo(4)          fibo(3)
          /     \          /     \
      fibo(3)  fibo(2)  fibo(2)  fibo(1)
      /     \     |        |        |
  fibo(2) fibo(1) 1        1        1

    |       |
    1       1
"""