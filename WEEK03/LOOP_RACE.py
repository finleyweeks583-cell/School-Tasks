import time
start = time.perf_counter()
total = 0
for number in range(10_000_000):
    total = total + number 
print(f"Loop:   {time.perf_counter() - start:.2f} seconds")
start = time.perf_counter()
total = sum(range(10_000_000))
print(f"sum(): {time.perf_counter() - start:.2f} seconds")