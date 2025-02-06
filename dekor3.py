class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {} 
    def __call__(self, *args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        print(f"Calculating the product of two numbers ({args})... ")
        if key not in self.cache:
            print(f"Processing calculation (no data in cache for args {key}... ")
            self.cache[key] = self.func(*args, **kwargs)
        else:
            print(f"Retrieving result from cache for args {key}... ")
        return self.cache[key]
@CacheResult
def calculate_multiply(a, b):
    return a + b
print(calculate_multiply(3, 5))  
print(calculate_multiply(3, 5)) 
print(calculate_multiply(2, 4))  
print(calculate_multiply(2, 4))  
