# how many crorepati?
kitna_paisa_hai=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
sum=0
sum_1=0
sum_2=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=100000000:
        sum=sum+1
    elif kitna_paisa_hai[i]>=10000000:
        sum_1=sum_1+1
    else:
        sum_2=sum_2+1 
    i+=1
print("crrorepati",sum)
print("lakhpati",sum_1)
print("dilwale",sum_2)


    