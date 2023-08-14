class Person():
    def __init__(self, name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single):
        self.name = name
        self.enter_time = 0
        self.exit_time = 0
        self.expected_monthly_working_hour = expected_monthly_working_hour
        self.salary_base = salary_base
        self.basic_overtime_pay =basic_overtime_pay
        self.monthly_working_hours = 0
        self.overtime_hour = 0
        self.find = find
        self.married_or_single = married_or_single
        self.total_salary = salary_base
        

    def set_enter_time(self, enter_time):
        self.enter_time = enter_time
        print(enter_time)


    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        self.monthly_working_hours += self.exit_time - self.enter_time
        print(exit_time)


    def time_calculation(self):
        # print(" runing in time_calculation() ")
        self.overtime_hour = self.monthly_working_hours - self.expected_monthly_working_hour
        # print(" finish time_calculation()")


    def salary_calculation(self):
        # print(" runing in salary_calculation() ")
        salary_dict = {}

        self.time_calculation()

        if self.overtime_hour >= 0 :
            over_time_salary = self.overtime_hour * self.basic_overtime_pay
            self.total_salary += over_time_salary
            salary_dict["over time"] = over_time_salary
        else:
            find_salary = self.overtime_hour * self.find
            self.total_salary +=  find_salary
            salary_dict["find"] = find_salary
            
        # print(" finish salary_calculation()")
        if self.married_or_single == "married":
            self.total_salary += 0.1 * self.salary_base
        # return self.total_salary
    

    def __str__(self):
        message = " {} monthly working hours is <<{}>>".format(self.name, self.monthly_working_hours)
        return message
    

    def print_pay_slip(self):
        # print(" runing in pay_slip() ")
        x,y = self.salary_calculation()

        print("salary base: +{} $".format(self.salary_base))
        if self.overtime_hour >= 0:
            print("overtime: +", self.overtime_hour * self.basic_overtime_pay)
        else:
            print("find:", self.overtime_hour * self.find)

        if self.married_or_single == "married":
            print("married: + ", 0.1 * self.salary_base)

        if x != None:
            print("work_experience: $", x)
        
        if y != None:
            print("education: $", y)

        
        print("---------------")
        print("Totla Salary: ", self.total_salary)
        # print(" finish pay_slip()")



class Employee(Person):
    def __init__(self, name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, work_experience, education ):
        super().__init__(name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single)

        self.work_experience = work_experience
        self.education = education
        
 
    def apply_work_experience(self):
        temp =  0
        if  20 > self.work_experience > 10:
            temp = 0.05 * self.salary_base
        elif self.work_experience > 20:
            temp = 0.1 * self.salary_base

        self.total_salary += temp

        return temp

    
        # print("******", self.total_salary)

    def apply_education(self):
        temp1 = 0
        if self.education == "master":
            temp1 = 0.05 * self.salary_base
        elif self.education == "bsc":
            temp1 = 0.03 * self.salary_base

        self.total_salary += temp1

        return temp1
        
        # print("******", self.total_salary)

    def salary_calculation(self):

        super().salary_calculation()
        education_bounes = self.apply_education()

        work_exp_bounes = self.apply_work_experience()
        return work_exp_bounes, education_bounes


    # def print_pay_slip(self):
    #     super().print_pay_slip()
        

       



    




# class Manager(Employee):
#     def __init__(self, name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, work_experience, education):
#         super.__init__(name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, work_experience, education)
        







