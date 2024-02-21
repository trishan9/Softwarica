import pdb

pdb.set_trace()
data = eval(input("Enter some data: "))
print(data, type(data))

# Conditional Statements
pocket_money = int(input("Enter your pocket money: "))
if pocket_money > 1000:
    print("With Sita")
else:
    print("With Gita")

days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

try:
    day = int(input("Enter the day in number: "))
    print(days[day])
except:
    print("Invalid")
