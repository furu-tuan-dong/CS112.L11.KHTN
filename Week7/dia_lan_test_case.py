import numpy as np
import itertools
import os


def check_result(k_items): # check if the combination is satisfy or not
    res = k_items[0]
    for item in k_items:
        res = res&item
    if res == 0:
        return True
    else:
        return False


def brute_force(arr, k): # loop through all the combinations in the array and find the possible outcome
    combinations = itertools.combinations(arr, k)
    for combination in combinations:
        if check_result(combination):
            return "YES", combination
    return "NO", None


def generate_arr_elements(n, k, lower_bound, upper_bound): # 0 ≤ elements < 2^12 
    arr = np.random.randint(low=lower_bound, high=upper_bound + 1, size=n)
    return arr


def generate_multiple_tests(lower_bound_testcase, upper_bound_testcase, num_tests, filename, \
                            low_ai=0, high_ai=4095):
    ns = np.random.randint(low=lower_bound_testcase, high=upper_bound_testcase, size=num_tests)
    f = open(filename, "a")
    for i in range(len(ns)):
        k = np.random.randint(low=1, high=ns[i]+1) 
        arr = generate_arr_elements(ns[i], k, low_ai, high_ai)
        output, explain = brute_force(arr, k)
        arr = ' '.join(map(str, arr)) # convert array to string
        print(f'Input:\n{ns[i]} {k}\n{arr}\nOutput:\n{output}')
        f.write(f'Input:\n{ns[i]} {k}\n{arr}\nOutput:\n{output}\n')
        if explain:
            print('Explain:\nk elements are:', explain)
            f.write('Explain:\nk elements are: ' + str(explain).replace("(", "").replace(")", "") + "\n")
    f.close()

if __name__ == "__main__":
    distributions = [0, 100, 10000, 20000] # 1 ≤ n ≤ 2×10^4
    filename = "result.txt"
    f = open(filename, "a")
    for i in range(len(distributions) - 1):
        print("10 tests from {} to {}".format(distributions[i] + 1, distributions[i+1]))
        f.write("10 tests from {} to {}".format(distributions[i] + 1, distributions[i+1]))
        generate_multiple_tests(distributions[i] + 1, distributions[i+1], 10, filename)
    f.close()