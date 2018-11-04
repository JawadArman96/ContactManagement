import EmployeeInfo
import UserInfo
class UserAction :
    def __init__(self,name):
        """"Initialize UserAction function"""
        self.name=name
        self.employee=EmployeeInfo.EmployeeInfo("Okay")
        self.employeeList=[]
    def showEmployee(self,employee):
        """Shows the information of an employee"""
        print("#####")
        print("Name: "+employee.name)
        print("Designation: "+employee.designation)
        print("Department: "+employee.department)
        if(employee.lead==1):
            print("Lead")
        elif employee.manager==1:
            print("Manager")
        print("Present Address: "+employee.presentAddress)
        print("Mobile Number: "+employee.mobileNumber)
        print("Permanent Address: "+employee.permanentAddrees)
        print("Emergency Contact: "+employee.emergencyContact)
        print("Email: "+employee.email)

    def showEmployees(self):
        """"Interate over employee list and call showEmployee function"""
        for emp in self.employeeList:
            self.showEmployee(emp)
    def insertEmployee(self):
        """Insert an employee to the list"""
        print("Enter the name of employee:")
        name=str(raw_input())
        employee=EmployeeInfo.EmployeeInfo(name)
        print("Enter the designation of the employee:")
        employee.designation=str(raw_input())
        print("Enter the department:")
        employee.department=str(raw_input())
        print("Enter 1 if Lead/0 if not:")
        employee.lead=int(raw_input())
        print("Enter 1 if Manager/0 if not:")
        employee.manager=int(raw_input())
        print("Enter present address:")
        employee.presentAddress=str(raw_input())
        print("Enter mobile number:")
        employee.mobileNumber=str(raw_input())
        print("Enter permanent address:")
        employee.permanentAddrees=str(raw_input())
        print("Enter emergency contact number:")
        employee.emergencyContact=str(raw_input())
        print("Enter email:")
        employee.email=str(raw_input())
        self.employeeList.append(employee)
        return employee
    def updateEmployee(self):
        """Updates information of the employeee"""
        emp=self.searchEmployee()
        if emp!="NULL":
            print("Enter the designation of the employee:")
            emp.designation = str(raw_input())
            print("Enter the department:")
            emp.department = str(raw_input())
            print("Enter 1 if Lead/0 if not:")
            emp.lead = int(raw_input())
            print("Enter 1 if Manager/0 if not:")
            emp.manager = int(raw_input())
            print("Enter present address:")
            emp.presentAddress = str(raw_input())
            print("Enter mobile number:")
            emp.mobileNumber = str(raw_input())
            print("Enter permanent address:")
            emp.permanentAddrees = str(raw_input())
            print("Enter emergency contact number:")
            emp.emergencyContact = str(raw_input())
            print("Enter email:")
            emp.email = str(raw_input())
        else:
            print("Employee not found")
    def deleteEmployee(self):
        """Deletes employee from employee list"""
        emp=self.searchEmployee()
        if emp.name!="NULL":
            self.employeeList.remove(emp)
    def searchEmployee(self):
        """Searches employee in the employee list"""
        empl=EmployeeInfo.EmployeeInfo("NULL")
        print("Enter the name of employee:")
        name=str(raw_input())
        for emp in self.employeeList:
            if name==emp.name:
                print("Employee found")
                return  emp
        print("Employee not found")
        return empl
# for i in range(0,2):
#     ob=UserAction("this")
#     ob.insertEmployee()
# ob.showEmployees()