class Company:
    
    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.n_employees = 0
        self.list_employees = []
    
    def add_employee(self, employee):
        self.list_employees.append(employee)
        self.n_employees += 1
    
    def show_employees(self):
        print("*** COMPANY NAME:", self.name.upper(), ' ***')
        print("    Number of employees:", self.n_employees, ' \n')
        for obj in self.list_employees:
            obj.print_profile()
        print("")

class Employee:
    
    # constructor
    def __init__(self, name, starting_date, salary):
        self.name = name
        self.starting_date = starting_date
        self.salary = salary
    
    # function
    def print_profile(self):
            print(self.name,":","( $",self.salary,"); started on",self.starting_date)