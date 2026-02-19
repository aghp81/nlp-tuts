#   یه برنامه بنویس که یه لیست از کاربر دریافت کنه و عناصر اضافی لیست لیست رو حذف کنه.

# یک لیست را از کاربر دریافت می‌کند

# عناصر تکراری (اضافی) را حذف می‌کند

# ترتیب اولیه عناصر را حفظ می‌کند (نکته مهم در بسیاری از کاربردها)

def remove_duplicates(input_list):
    seen = set()
    result = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# دریافت لیست از کاربر
user_input = input("عناصر لیست را با کاما جدا کنید: ")
user_list = user_input.split(",")

# حذف فاصله‌های اضافی
user_list = [item.strip() for item in user_list]

# حذف عناصر تکراری
clean_list = remove_duplicates(user_list)

print("لیست نهایی بدون عناصر تکراری:")
print(clean_list)

# ورودی:
# apple, banana, apple, orange, banana

# خروجی:
# ['apple', 'banana', 'orange']


# اگر ترتیب عناصر مهم نیست
user_input = input("عناصر لیست را با کاما جدا کنید: ")
user_list = user_input.split(",")

clean_list = list(set(item.strip() for item in user_list))

print(clean_list)


user_input = input("اعداد را با کاما جدا کنید (مثال: 1,2,3,2,4): ")

# تبدیل ورودی به لیست عددی
number_list = [int(item.strip()) for item in user_input.split(",")]

# حذف عناصر تکراری
clean_list = list(set(number_list))

print("لیست نهایی بدون عناصر تکراری:")
print(clean_list)


# ورودی:
# 1, 2, 3, 2, 4, 1

# خروجی (ترتیب ممکن است متفاوت باشد):
# [1, 2, 3, 4]
