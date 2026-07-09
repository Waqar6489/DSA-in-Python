def clean(name):
    left= 0
    for right in range(1,len(name)):
        if name[right]!=name[left]:
            left=left + 1
            name[left]=name[right]
    return left + 1
    
names= ["ammar","abu","bee","bee","chudury","chudury","esha","esha"]   
count = clean(names)
print(names[:count])

"""
Rules:
Same name ? right move ,left stay, register change does not
Different name ? left move, new name copy left new spot
"""