#Variable
salary=0
net_salary=0
first=0 #
second=0
third=0
tax=0

#Input
salary=int(input("Ender the Monthly Gross Salary : "))

#process and output
if (0<salary<=99999):
    net_salary=salary
    print("Net Salary ",net_salary)

elif(100000<=salary<=150000):
    first=salary-99999
    tax=first*5/100
    net_salary=salary-tax
    print("Net Salary ",net_salary)
    
elif(150001<=salary<=250000):
    first= salary-99999
    second=first-50001
    tax=50001*5/100 + second*10/100
    net_salary=salary-tax
    print("Net Salary ",net_salary)
    
elif(salary>250000):
    first= salary-99999
    second=first-50001
    third=second-100000
    tax=50001*5/100 + 100000*10/100 + third*12/100
    net_salary= salary-tax
    print("Net Salary ",net_salary)

else:
    print("Wrong Input")