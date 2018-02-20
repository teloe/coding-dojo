list = ['hello','world','my','name','is','Anna']
char = 'o'

n=[]
count=0
for item in list:
    if char in item:
        n.append(item)
print n
