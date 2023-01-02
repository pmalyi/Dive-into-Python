from solution import FileReader
with open('example.txt', 'w') as file:
    file.write('some text')
reader = FileReader('example.txt')
text = reader.read()
print(text)
print(type(reader))
