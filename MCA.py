sol_name=[]
criteria_val=[]
criteria_weight=[]
criteria_name=[]
criteria_val.append([])
criteria_val.append([])
sum=[]

c=input("\t\tMulti-Criteria Analysis\n\nEnter number of criterias : ")
for i in range(c):
    criteria_name.append(raw_input("Enter criteria %d name: "%(i+1)))
for i in range(c):
    criteria_weight.append(input("Enter %s weight: "%criteria_name[i]))
n=input("\nEnter number of possible solutions: ")

for i in range(n):
    for j in range(c):
        criteria_val[i].append(0)
    sum.append(0)

for i in range(n):
    sol_name.append(raw_input("\nEnter solution %d name: "%(i+1)))     
    ch=[]
    for j in range(c):
        criteria_val[j][i]=input("Enter value of %s: "%criteria_name[j])

for i in range(n):
    div=float(max(criteria_val[i]))
    for j in range(c):
        criteria_val[i][j]*=criteria_weight[i]/div

for i in range(n):
    for j in range(c):
        sum[i]+=criteria_val[j][i]

i=sum.index(max(sum))    
print("\nThe most optimal solution is %s"%sol_name[i])
v=raw_input(" ")
