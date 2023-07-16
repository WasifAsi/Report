#Variable
salary=0
net_salary=0

#Input
salary=int(input("Ender the Monthly Gross Salary : "))

#process and output
if (0<salary<=99999):
    net_salary=salary
    print("Net Salary ",salary)

elif(99999<salary<=150000):
    net_salary=salary*95/100
    print("Net Salary ",net_salary)
    
elif(150000<salary<=250000):
    net_salary=salary*90/100
    print("Net Salary ",net_salary)
    
elif(salary>250000):
    net_salary= salary*88/100
    print("Net Salary ",net_salary)
    
else:
    print("Wrong Input")