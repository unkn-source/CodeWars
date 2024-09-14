import random

def find_random_seed(lst):
    for seed in range(10000):
        random.seed(seed)
        generated_list = [random.randint(0, 100) for _ in range(10)]
        if generated_list == lst:
            return seed
    return None