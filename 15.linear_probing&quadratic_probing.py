def linear_probing(hash_table, element):
    index = element%size
    i=1
    while hash_table[index] is not None:
        index = (index+i)%size
        i+=1
    hash_table[index] = element

def quadratic_probing(hash_table, element):
    index = element%size
    i=1
    while hash_table[index] is not None:
        index = (index+i*i)%size
        i+=1
    hash_table[index] = element

size = int(input())
elements = []
print()

hash_table_linear = [None]*size
hash_table_quadratic = [None]*size

for i in range(size):
    elements.append(int(input()))

print("Hash Table Using Linear Probing:")
for element in elements:
    linear_probing(hash_table_linear, element)

for i in range(size):
    print(f"{hash_table_linear[i]}")

print("Hash table using Quadratic probing:")
for element in elements:
    quadratic_probing(hash_table_quadratic,element)

for i in range(size):
    print(f"{hash_table_quadratic[i]}")