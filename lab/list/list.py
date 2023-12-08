my_list = [1, 'two', 'a', 4, 'a']
my_list.sort(key=lambda val: val == 'a')
print(my_list)