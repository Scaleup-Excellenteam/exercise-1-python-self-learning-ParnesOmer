#2000_running
import time

def running_2000(f, *parameters):
    t_start = time.time()
    try:
        f(*parameters)
    except Exception as e:
        print(f"Error: {e}")
    t_end = time.time()
    return t_end - t_start

if __name__ == "__main__":
    running_2000(print, "Hello")
