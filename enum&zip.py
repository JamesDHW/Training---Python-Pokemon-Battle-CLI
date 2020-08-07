f_names = ['Jack', 'James', 'Zac']
l_names = ['Doyle', 'Haworth Wheatman', 'Lewis']
for i, zipped in enumerate(zip(f_names, l_names)):
    first, last = zipped
    print(f'The name at index {i} is {first} {last}')
