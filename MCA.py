import numpy as np
import matplotlib.pyplot as plt

c=int(input("\t\tMulti-Criteria Analysis\n\nEnter number of criterias : "))
criteria_name=np.empty(c,object)
criteria_weight=np.empty(c,float)
for i in range(c):
    criteria_name[i]=input(f"Enter criteria {i+1} name: ")
for i in range(c):
    criteria_weight[i]=float(input(f"Enter {criteria_name[i]} weight: "))

n=int(input("\nEnter number of possible solutions: "))
criteria_val=np.empty((c,n),float)
sum=np.empty(n,float)
sol_name=np.empty(n,object)

for i in range(n):
    sol_name[i]=input(f"\nEnter solution {i+1} name: ")     
    for j in range(c):
        criteria_val[j][i]=float(input(f"Enter value of {criteria_name[j]}: "))

for i in range(n):
    div=criteria_val[i].std()
    for j in range(c):
        criteria_val[j][i]*=criteria_weight[i]/div

for i in range(n):
    for j in range(c):
        sum[i]+=criteria_val[j][i]

i=sum.argmax()   
print(("\nThe most optimal solution is %s"%sol_name[i]))

ind=np.arange(n)
p=np.empty(n,dtype=object)
p[0] = plt.bar(ind, criteria_val[0])
for i in range(1,n):
    p[i] = plt.bar(ind, criteria_val[i],bottom=criteria_val[i-1])
plt.xticks(ind,sol_name)
plt.legend(criteria_name)
plt.show()