# Recursion mean call itself when the thing are empty 
# Stop the condition in recursion is Base Case

def recursion(count):
    # BASE CASE: Stop the function when count hits 0
    if count == 0:
       print("I have empty hand because I'm eat all.")
       return # 👈 CRITICAL: This exits the function immediately

    # RECURSIVE CASE: Run this as long as count is greater than 0
    print(f"I have a {count} apple and now eat one.")
    recursion(count-1) 

recursion(5)


def recursion(count):
    if count == 0:
       print("I have empty hand because I'm eat all.")
    else:
       print(f"I have a {count} apple and now eat one.")
       recursion(count-1) 

recursion(5)