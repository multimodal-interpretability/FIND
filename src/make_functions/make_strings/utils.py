import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # get the current time
        result = func(*args, **kwargs)  # call the original function
        end_time = time.time()  # get the current time again
        print(f"Time elapsed for {func.__name__}: {end_time - start_time} seconds.")
        return result  # return the result of the original function
    return wrapper