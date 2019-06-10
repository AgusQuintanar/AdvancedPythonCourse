
def generateColumn(column):
    columna, *datos = column
    print("Column name:",columna)
    print("Data:",datos)

names = ['names','agustin','andres','hector','ari','daniel','paco']
lastNames = ['last names','quintanar','diaz de leon','alvarez','valenzuela','velazquez','valencia']

generateColumn(names)
generateColumn(lastNames)
        #  name       last name    current semester  age   expected graduation date
student = ['agustin','quintanar', 'second semester', '19', (10,12,2022)]

name, *ignored, (*ignored ,expected_graduation_year) = student

print('Student name:',name)
print('Expected graduation year:',expected_graduation_year)