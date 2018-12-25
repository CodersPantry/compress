s=input("Enter a string:")
count=1
ls=[]
for i in s:
    if (s.index(i)+1)==len(s):
        pass
    else:
        if i==s[s.index(i)+1]:
            count+=1
        else:
            ls.append('{}:{}'.format(i,count))
            count=1
print(ls)
