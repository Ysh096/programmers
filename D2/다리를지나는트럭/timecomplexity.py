import timeit
start_time = timeit.default_timer()

test_list = [1, 2, 3]

for _ in range(10000):
    test_list = [0] + test_list
    # test_list.insert(0, 0)

terminate_time = timeit.default_timer()

print('덧셈: ', terminate_time - start_time)


start_time = timeit.default_timer()

test_list = [1, 2, 3]
print('insert 전: ', id(test_list))
for _ in range(10000):
    # test_list = [0] + test_list
    test_list.insert(0, 0)

terminate_time = timeit.default_timer()
print('insert 후: ', id(test_list))
print('insert:', terminate_time - start_time)