import random
import time


first = "حجرة"
second = "ورقة"
third = "مقص"

options = [first, second , third]

user_input = input("Enter your option: ")  #هني اختيار المستخدم

selected = random.choice(options)  # هني اختيار الكمبيوتر العشوائي

if selected == user_input:
    time.sleep(3)  #تأخير 3 ثواني قبل الطباعة
    print(selected)
    time.sleep(2)
    print("تعادل")
    #الحالات التي يكون فيها الكمبيوتر هو الخاسر والمستخدم الرابح
elif (selected == "مقص" and user_input == "حجرة") or (selected == "حجرة" and user_input == "ورقة") or (selected == "ورقة" and user_input == "مقص"):
    time.sleep(3)
    print(selected)
    time.sleep(2)
    print("انت ربحت")
    #الحالات التي يكون فيها المستخدم الخاسر والكمبيوتر الرابح
elif (selected == "مقص" and user_input == "ورقة") or (selected == "حجرة" and user_input == "مقص") or (selected == "ورقة" and user_input == "حجرة"):
    time.sleep(3)
    print(selected)
    time.sleep(2)
    print("اني فزت GG")
else:
    time.sleep(3)
    print("القيمة المدخلة غير مفهومة")
    