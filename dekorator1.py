def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__} with: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
@log_function_call
def multiply_numbers(x, y):
    return x * y
result = multiply_numbers(3, 5)
print("Result:", result) 
