# UNION
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3)


# INTERSECCION
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 & my_set2
print(my_set3)


# DIFERENCIA
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 - my_set2
print(my_set3)

my_set4 = my_set2 - my_set1
print(my_set4)


# DIFERENCIA SIMETRICA
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 ^ my_set2
print(my_set3)