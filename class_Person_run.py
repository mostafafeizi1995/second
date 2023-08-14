from class_Person import *


x = Manager("mostafa", 25, 500, 150, 200, "married", 13, "master", 60, 120)

for i in range(3):
    x.set_enter_time(int(input("Enter Time: ")))
    x.set_meeting_hour(int(input("Meeting Time: ")))
    x.set_mission_hour(int(input("Mission Time: ")))
    x.set_exit_time(int(input("Exit Time: ")))

# # x.print_pay_slip()
# x = Employee("Mohammad Ardestani", 20, 15000, 200, 50, "married", 15, "master", )
# x = Person("Mohammad Ardestani", 20, 15000, 200, 50, "married")


# # x.set_enter_time(8)
# x.set_exit_time(17)
# # print(x)

# x.set_enter_time(8)
# x.set_exit_time(15)
# # print(x)

# x.set_enter_time(11)
# x.set_exit_time(17)
# print(x)

# # # x.set_enter_time(9)
# # # x.set_exit_time(17)
# # # print(x)


x.print_pay_slip()


# # employee2 = Employee("x", 32, 500, 30, 50, "married", 12, "diploma")

# # print(employee2)