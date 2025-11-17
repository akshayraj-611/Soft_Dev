import random
import time
sizes = [10000, 100000, 500000, 1000000 ] 
interval_max = 10000000  
n_queries = 1000

for size in sizes :
    print(f"\n Testing with {size} elements....")
    my_list = random.sample(range(interval_max), size)
    my_set = set(my_list)

    queries = [random.randint(0, interval_max) for _ in range(n_queries)]
    start_list = time.perf_counter()
    for q in queries:
        _ = q in my_list 
    end_list = time.perf_counter()   
    list_time = end_list - start_list

    start_set = time.perf_counter()
    for q in queries:
        _ = q in my_set  
    end_set = time.perf_counter()
    set_time = end_set - start_set
    print(f"  List time: {list_time:.6f} seconds")
    print(f"  Set  time: {set_time:.6f} seconds")
    print(f"  Speedup:  {list_time / set_time:.1f}x faster using a set")

