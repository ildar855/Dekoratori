import time
class RateLimiter: 
    def __init__(self, max_calls, period): 
        self.max_calls = max_calls 
        self.period = period 
        self.calls = [] 
    
    def __call__(self, func): 
        def wrapper(*args, **kwargs): 
            current_time = time.time()
            self.calls = [call for call in self.calls if call > current_time - self.period]
            
            if len(self.calls) >= self.max_calls:
                raise RuntimeError("Error occurred: Rate limit exceeded. Please try again later.")
            self.calls.append(current_time)
            return func(*args, **kwargs) 
        return wrapper 
@RateLimiter(max_calls=6, period=10) 
def api_call(): 
    print("API call executed successfully...")  
for _ in range(8): 
    try: 
        api_call() 
    except Exception as e: 
        print(f"Error occurred: {e}") 
time.sleep(10) 
api_call() 
