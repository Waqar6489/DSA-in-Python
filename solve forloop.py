# n=5
# factorial= 1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

# num=125
# is_prime=True
# for i in range(2,int((num**0.5)+1)):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime and num>1:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")
    

word="python"
dict={}
for i in word:
    if i in dict:
        dict[i]+=1
        
    else:
        dict[i]=1

for char , val in dict.items():
    print(char + ":",val)