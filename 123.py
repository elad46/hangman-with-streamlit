
# תרגיל בדיקת גיל
# name = input("מה שמך? ")
# print("שלום, " + name + "!")
#
# age = int(input("בן כמה אתה ?"))
# if age >= 18:
#     print("מותר לך לנהוג ..")
# elif age > 16:
#     print("יכול ללמוד תאוריה .")
# else:
#     print("אסור לך לנהוג !!! ")
from functools import total_ordering

# print(f"name +  age")



# # 1
# name = input("מה השם שלך ?")
# age = int(input("בן כמה אתה ?"))
# print(f"  שלום {name},אתה בן {age}")



# # 2 האם מספר זוגי או לא
# num = int(input("תן מספר "))
# if num % 2 == 0:
#     print("המספר הוא זוגי .")
# else:
#     print("המספר הוא אי זוגי")




# # 3 כניסה למועדון
# age = int(input("מה הגיל שלך ?"))
# if age >= 18:
#     print("ברוך הבא .")
# else:
#     print("הכניסה אסורה.!")



# # 4 בדיקת ציונים
# test = int(input("מה הציון שלך ?"))
#
# if test < 55:
#     print("נכשלת !")
# elif 55 <= test < 75:
#     print("עברת ")
# elif 75 <= test < 90:
#     print("טוב מאוד")
# else:
#     print("מצוין")



# # 5 חישוב סכום ספרות שמקבל מהמשתמש
# number = int(input("הכנס מספר: "))
# sum_digits = 0
#
# while number > 0:
#     digit = number % 10
#     sum_digits += digit
#     number = number // 10
#
# print("סכום הספרות הוא:", sum_digits)



# # 6    Rectangle area calc
#
# len = float(input("Enter the length: "))
# wid = float(input("Enter the width: "))
# area = len * wid
#
# print(f"the area is: {area}cm")


# # 9  bmi
# weight = float(input("מה המשקל שלך: "))
# height = float(input("מה הגןבה שלך: "))
# bmi = weight / (height ** 2)
#
# bmi_rounded = round(bmi, 2)
# print(f"the {bmi_rounded} ")
#
# if bmi < 18.5:
#     category = "תת-משקל"
# elif 18.5 <= bmi < 25.0:
#     category = "משקל תקין"
# elif 25.0 <= bmi < 30.0:
#     category = "עודף משקל"
# else: # bmi >= 30.0
#     category = "השמנת יתר"
#
# print(f"אתה נמצא בקטגוריית: {category}.")



#  22 shopping cart progrem

# item = input("מה המוצר שאתה רוצה לקנות ?")
# price = float(input("מה המחיר: "))
# quantity = int(input("מה כמות המוצרים: "))
# total = price * quantity
# discount = int(input("מה אחוז ההנחה שיש לך: "))
#
# amount = total * (discount / 100)
# price_after_discount = total - discount
#
# print(f"you have bought {quantity} * {item}")
# print(f"עלות הקנייה: שח{total}")
# print(f"the price: {total} - {discount}")

# 27  random numbers
import random

number = random.randint(1,100)
print("נחש מספר בין 1 ל-100")
guess =


# 24  quiz game
