s=input("Enter a string:")
count=1
ls=[]
for i in range(len(s)):
    if i+1==len(s):
            pass
    elif s[i]==s[i+1]:
        count+=1
    else:
        print('{}:{}'.format(s[i-1],count))
        count=1
#print(ls)
