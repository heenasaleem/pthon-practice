class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

      Employee.empCount += 1
   def __del__(self):
         print "destuctor called"
         pass
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary 

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.__del__()
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp2.salary = 20;
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount
print "disp attributes", hasattr(emp1 , 'salary') 
