# hash is a technique
#a) hash table in which store value in key and value
#b) hash function , used in python build_in
# hash function used in python is dict and set  
# Complexity is O(1)

"""
A Hash Table (or Hash Map) is a data structure that stores information in key-value pairs, 
acting like a dictionary where you look up a word (key) to find its definition (value).
It is one of the most important concepts in Data Structures and Algorithms (DSA) 
because it allows you to search, insert, and delete data in O(1) constant time on average.
1. How Hashing WorksInstead of searching through an entire array index by index, 
a hash table uses a Hash Function to instantly calculate exactly where a piece of data should go.

[ Key: "apple" ]  ───►  ( Hash Function )  ───►  Index: 4  ───►  [ Array Slot 4: 150 ]

Key: The unique identifier you want to look up (e.g., a student's name, a username).
Hash Function: A mathematical algorithm that takes the key and converts it into an integer index.
Value: The data associated with that key (e.g., student grades, account details).
Bucket/Slot: The position in the underlying array where the value is stored.

2. The Problem of Collisions
Because an array has a fixed size, a hash function might sometimes output the same index 
for two different keys. This is called a Collision.
DSA uses two primary techniques to handle collisions:
Chaining (Open Addressing): Each slot in the array points to a Linked List. If two keys 
land on the same index, they are chained together in that list.
Open Addressing: The hash table looks for the next empty available slot in the array 
using methods like Linear Probing (checking the next slot +1, +2, +3...) or Quadratic Probing.
"""

data=[
    "ali@gmail.com",
    "ammar@gmail.com",
    "hamid@gmail.com",
    "ammar@gmail.com",
]

def remove_duplicate(emails):
    seen=set() # if check set / dict O(1)
    lists=[] # if check list O(n)
    for email in emails:
        if email not in seen: # check set not list if check list then take time is O(n)
            seen.add(email)
            lists.append(email)
    return lists

print(remove_duplicate(data))    


data=[
    "ali@gmail.com",
    "ammar@gmail.com",
    "hamid@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
    "ammar@gmail.com",
]

def handle_coll(emails):
    dic={}
    for email in emails:
        if email in dic:
            dic[email] = dic[email] +1
        else:
             dic[email] = 1
    return dic            

print(handle_coll(data))    

