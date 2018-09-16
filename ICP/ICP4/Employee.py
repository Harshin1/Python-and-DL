class Employee(object):
    numEmp = 0;
    totalSal = 0;
    def __init__(self):
        Employee.numEmp += 1

    def __init__(self,name,family, salary, dept):
        Employee.numEmp += 1
        self.name = name
        self.family = family
        self.salary = salary
        self.dept = dept
        Employee.totalSal += salary

    def average(self):
        return Employee.totalSal/Employee.numEmp

class FullTimeEmployee(Employee):
    def __init__(self):
        super(Employee, self).__init__()

    def __init__(self, name, family, salary, dept):
        Employee.__init__(self,name,family, salary, dept)

emp = FullTimeEmployee('Harshini', 2, 100, 'ABC')
e = Employee('Hars', 1, 300, 'ACB')
print('Number of employees are: ' + str(emp.numEmp))
print('Salary of employee is ' + str(emp.salary))
print('Average salary of employees: ' + str(emp.average()))
