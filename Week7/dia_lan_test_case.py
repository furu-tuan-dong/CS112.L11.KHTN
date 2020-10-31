import numpy as np
import itertools


def check_result(k_items):
    res = k_items[0]
    for item in k_items:
        res = res&item
    if res == 0:
        return True
    else:
        return False


def brute_force(arr, k):
    combinations = itertools.combinations(arr, k)
    for combination in combinations:
        if check_result(combination):
            return "YES", combination
    return "NO", None


def generate_rules(n, k, lower_bound, upper_bound):
    arr = np.random.randint(low=lower_bound, high=upper_bound + 1, size=n)
    return arr


def generate_multiple_tests(low_n, high_n, num_tests, low_ai=0, high_ai=4095):
    ns = np.random.randint(low=low_n, high=high_n, size=num_tests)
    for i in range(len(ns)):
        k = np.random.randint(low=1, high=ns[i]+1)
        arr = generate_rules(ns[i], k, low_ai, high_ai)
        output, explain = brute_force(arr, k)
        print(f'Input:\n{ns[i]} {k}\n{arr}\nOutput:\n{output}')
        if explain:
            print('Explain:\nk elements are:', explain)
        print()


if __name__ == "__main__":
    generate_multiple_tests(low_n=1, high_n=20, num_tests=3)
