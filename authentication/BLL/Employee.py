from ..modelManager import EmployeeSerializer


class Employee:
    def __init__(self, email, username, password, DateOfBirth, CITIZENSHIP_NO, Address, Phone_No, Employee_Type):
        self.E1 = EmployeeSerializer(email, username, password, DateOfBirth, CITIZENSHIP_NO, Address, Phone_No, Employee_Type)