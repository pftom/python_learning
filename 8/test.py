def test_one(test_dict):
    """for test pass dict"""
    return test_dict


# test pass dict
test_one_dict = {'a': 'a'}
test_one(test_one_dict)

# test pass list
test_one_list = [1, 2]
test_one(test_one_list)

# return list
test_return_list = test_one(test_one_list)
print(test_return_list)
