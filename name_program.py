#FirstFunction
with open('name.txt') as f:
     name = f.read()

print(name)

#SecondFunction 
with open('hello.txt', 'w') as f:
    f.write('hello  my name is'+name + ".")
    f.write('\n')