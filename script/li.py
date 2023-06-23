nn = [100,200,300,400,500]
nn_copy = nn
nn[1] = 777
print(nn)
nn = nn_copy
nn[1] = [444,555]
print(nn)
nn = nn_copy
nn[1:4] = [444,555]
print(nn)
nn = nn_copy
nn[2:] = []
print(nn)
