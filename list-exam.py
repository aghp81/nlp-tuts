# سؤال ۱

# یک لیست شامل اعداد [1, 2, 3, 4, 5] دارید. چگونه عدد 10 را به انتهای لیست اضافه می‌کنید؟

numbers = [1, 2, 3, 4, 5]
numbers.append(10)
print(numbers)

# [1, 2, 3, 4, 5, 10]



# سؤال ۲

# فرض کنید لیست زیر را داریم. چگونه عنصر سوم آن را چاپ می‌کنید؟

items = ["apple", "banana", "cherry", "orange"]
print(items[2])

# cherry


# سؤال ۳

# چگونه می‌توان یک عنصر مشخص (مثلاً "banana") را از لیست حذف کرد؟

items = ["apple", "banana", "cherry"]
items.remove("banana")
print(items)

# ['apple', 'cherry']


# سؤال ۴

# برنامه‌ای بنویسید که جمع عناصر یک لیست عددی را محاسبه کند.
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)

# 100


# سؤال ۵

# چگونه می‌توان لیستی از اعداد زوج بین 1 تا 10 با استفاده از List Comprehension ایجاد کرد؟
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

[2, 4, 6, 8, 10]
