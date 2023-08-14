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
        # print("enter_time: ", enter_time)


    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        self.monthly_working_hours += self.exit_time - self.enter_time
        # print("exit_time: ", exit_time)

    def time_calculation(self):
        self.overtime_hour = self.monthly_working_hours - self.expected_monthly_working_hour

    def salary_calculation(self):
        salary_dict = {}
        salary_dict["base salary"] = self.salary_base
        self.time_calculation()

        if self.overtime_hour >= 0 :
            over_time_salary = self.overtime_hour * self.basic_overtime_pay
            self.total_salary += over_time_salary
            salary_dict["over time"] = over_time_salary
        else:
            find_salary = self.overtime_hour * self.find
            self.total_salary +=  find_salary
            salary_dict["find"] = find_salary

        if self.married_or_single == "married":
            married_salary = 0.1 * self.salary_base
            self.total_salary += married_salary
            salary_dict["married"] = married_salary

        return salary_dict
    

    def __str__(self):
        message = " {} monthly working hours is <<{}>>".format(self.name, self.monthly_working_hours)
        return message
    

    def print_pay_slip(self):

        print("---------------")
        salary_dict = self.salary_calculation()
        for key, val in salary_dict.items():
            print( key, ": ", val)
        
        print("---------------")
        print("Totla Salary: ", self.total_salary)

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

    
    def apply_education(self):
        temp1 = 0
        if self.education == "master":
            temp1 = 0.05 * self.salary_base
        elif self.education == "bsc":
            temp1 = 0.03 * self.salary_base

        self.total_salary += temp1

        return temp1
        

    def salary_calculation(self):

        salary_dict = super().salary_calculation()
        education_bounes = self.apply_education()
        work_exp_bounes = self.apply_work_experience()

        salary_dict["education"] = education_bounes
        salary_dict["work_exp"] = work_exp_bounes


        return salary_dict
       
class Manager(Employee):
    def __init__(self, name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, work_experience, education, meeting_salary_base, mission_salary_base):
        super().__init__(name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, work_experience, education)
        
        self.meeting_salary_base = meeting_salary_base
        self.mission_salary_base = mission_salary_base
        self.monthly_meeting_hour = 0
        self.monthly_mission_hour = 0



    def set_meeting_hour(self, meeting_time):
        self.monthly_meeting_hour += meeting_time  

    def set_mission_hour(self, mission_time):
        self.monthly_mission_hour += mission_time


    def salary_calculation(self):
        salary_dict = super().salary_calculation()
        meeting_bounes = self.monthly_meeting_hour * self.meeting_salary_base
        mission_bounes = self.monthly_mission_hour * self.mission_salary_base

        self.total_salary += meeting_bounes
        self.total_salary += mission_bounes

        salary_dict["meeting"] = meeting_bounes 
        salary_dict["mission"] = mission_bounes

        # self.monthly_meeting_hour***********************************************

        return salary_dict



class Intern(Person):
    def __init__(self, name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single, minimum_working_hours_per_month,fine_salary):
        super().__init__(name, expected_monthly_working_hour, salary_base, basic_overtime_pay, find, married_or_single)

        self.minimum_working_hours_per_month = minimum_working_hours_per_month
        self.fine_salary = fine_salary



    def set_fine_salary(self):
        fine = 0 
        if self.expected_monthly_working_hour < self.minimum_working_hours_per_month:
            fine = self.salary_base - self.salary_base * 90






    def Company_satisfaction(self):
        salary_dict = super().salary_calculation()
        
        if self.expected_monthly_working_hour < self.minimum_working_hours_per_month:
            salary_penalty = 0  
            salary_penalty = self.salary_base - self.salary_base * 90 

           
            return salary_dict
        
    
    def __str__(self):
       
        massege  = "The performance is not acceptable from the point of view of this company"
        return massege  






        

        

   


     


    
