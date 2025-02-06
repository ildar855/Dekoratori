import time
def measure_execution_time (func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()  
        elapsed_time = end_time - start_time

        print(f"Function {func.__name__} took {elapsed_time:.7f} seconds to execute")
        return result
    return wrapper
@measure_execution_time 
def calculate_multiply(numbers):
    tot = 1 
    for x in numbers: 
        tot *= x 
    return tot 
result = calculate_multiply([1, 2, 3, 4, 5, 6, 7, 8])
print("Result:", result) 
