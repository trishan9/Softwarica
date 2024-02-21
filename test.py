# # def LinearSearch(list, target):
# #     for i, item in enumerate(list):
# #         print(f"Step {i + 1}")
# #         if (item == target):
# #             return i
# #     else:
# #         return -1


# # def BinarySearch(list, target):
# #     low = 0
# #     high = len(list) - 1
# #     mid = 0
# #     steps = 0

# #     while low <= high:
# #         mid = (low + high) // 2
# #         steps += 1
# #         print(f"Step {steps}")

# #         if list[mid] < target:
# #             low = mid + 1

# #         elif list[mid] > target:
# #             high = mid - 1

# #         else:
# #             return mid
# #     else:
# #         return -1


# # print(LinearSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
# # print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))

# try:
#     print("Hello World")
# except:
#     print("Please")

# try:
#     print("Hello World")
# finally:
#     print("Hello")

# try:
#     print("Hello World")
# except:
#     print("Please")
# finally:
#     print("Hello")

# try:
#     print("Hello World")
# except:
#     print("Please")
# else:
#     print("Hello")


# try:
#     print("Hello World")
# except:
#     print("Please")
# else:
#     print("Please")
# finally:
#     print("Hello")


# assert condition, message


# def calculate_average(numbers):
#     assert len(numbers) > 0, "List must not be empty"
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average


# data = []
# result = calculate_average(data)
# print(result)

# fact = 1
# num = 4
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# print(fact)


string = input("Enter a string")
count_1 = 0
count_2 = 0
count_3 = 0
