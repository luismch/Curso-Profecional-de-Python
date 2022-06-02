#COMO SE CREAN LOS SETS
my_set = {3, 4, 5}
print("my_set =", my_set)

my_set2 = {"hola", 23.3, False, True}
print("my_set2 =", my_set2)

my_set3 = {3, 3, 2}
print("my_set3 =", my_set3)

my_set4 = {[1, 2, 3], 4}
print("my_set4 =", my_set4)


# CREAR SETS VACIOS
#python entiende que es un diccionario
empty_set ={}
print(type(empty_set))
#set vacio
empty_set= set()
print(type(empty_set))


#CASTING CON SETS
my_list = [ 1, 1, 2 .3, 4 ,4, 5]
my_set = set(my_list)
print(my_set)

my_tuple = ("hola", "hola", "hola", 1)
my_set2 = set(my_tuple)
print(my_set2)


# AÑADIR ELEMENTOS A UN SET
my_set={1, 2, 3}
print(my_set)

#Añadir un elemento
my_set.add(4)
print(my_set)

#añadir multiples elementos
my_set.update = ([1,2,5])
print(my_set)

#Añadir multiples elementos
my_set.update((1, 7, 2),{6,8})


#BORRAR ELEMENTOS DE UN SET
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

# Borrar un elemento existente
my_set.discard(1)
print(my_set)

# Borrar un elemento existente
my_set.remove(2)
print(my_set)

# Borrar un elemento inexistente - se puede eliminar un elemeto
#  no existente pero no pasa nada al ejecutarse
my_set.discard(10)
print(my_set)

# Borrar un elemento inexistente - se produce un error al eliminar un elemento 
# no existente
my_set.discard(12)
print(my_set)
