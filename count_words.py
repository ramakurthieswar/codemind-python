n=input()
count=0
vol="aeiouAEIOU"
res=n.split()
for i in res:
    if i[0] in vol and i[-1] not in vol:
        count=count+1
print(count)
    