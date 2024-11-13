employee=['SAM',"Ram","Chris"]
salary=[15000,5789000,5344567]
print(employee)
print(salary)
print(employee[0],salary[0])
print(employee[1],salary[1])
student=['sam','s1',[21,23,28]]
print(student[2][1])
my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i,end= "  ")


even_numbers=list(range(2,20,2))
print(even_numbers)
print(len(even_numbers))
for employees in employee:
    print("Happy New Year "+employees)
company_employees=employee+salary
print(company_employees)
binary=['ram','chris']
bytsequence=binary*5
print(bytsequence)
even=[4,0]
mul2=[2,4,4,4]
print(even==mul2)
print(even>mul2)
print(4 in even)