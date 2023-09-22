emp={}
ans='yes'
while(ans!='no'):
    name=input('enter the name of employee')
    salary=float(input('enter the salary of that employee'))
    emp[name]=salary
    ans=input('do you want add more employee')
print(emp)
