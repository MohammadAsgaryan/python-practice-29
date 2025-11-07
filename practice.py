import time

def timer_decorator(func):
    def wrapper(n):
        start = time.time()     # زمان شروع
        result = func(n)        # اجرای تابع اصلی
        end = time.time()       # زمان پایان
        
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper

@timer_decorator
def create_list(n):
    return list(range(1, n+1))

# دریافت ورودی از کاربر
try:
    num = int(input("Enter a number: "))
    output = create_list(num)
    print("Generated list:", output)
except ValueError:
    print("Invalid input! Please enter a number.")
