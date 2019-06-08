items = ['names','agustin','andres','hector','ari','daniel','paco']

columna, *datos = items

print(columna)
print(datos)

        #  name       last name    current semester  age   expected graduation date
student = ['agustin','quintanar', 'second semester', '19', (10,12,2022)]

name, *ignored, (*ignored ,expected_graduation_year) = student

print('Student name:',name)
print('Expected graduation year:',expected_graduation_year)