###### Numbers
# Addition
print(2+1)

# Subtraction
print(2-1)

# Multiplication
print(2*2)

# Division
print(3/2)

# Floor Division
print(7//4)

print(7%4)

print(2**4)

###### Variables

myVar = 4
print(myVar)

myVar = ["javi", "pepe"]

print(myVar)

string = 'Hello World'
print(string[-3:-2])
string = 'Hello World'[-3:-2]
print(string)
string = 'tinker'[1:4]
print(string)

print(string.capitalize())
print('Sammy'[2:])


print('*********************19. Print formatted strings')
print("I'm going to inject %s here." %'INJECTED')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x, y = 'SOME', 'MORE'
print("I'm going to inject %s text here, and %s text here."%(x,y))

print('The {2} {1} {0}'.format('fox','brown','quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))

print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:20.2f}'.format(13.579))


name = 'Fred'

print(f"He said his name is {name}.")

print('*********************21. Lists')
my_list = [1,2,3]
my_list2 = ['A string',23,100.232,'o']
print(my_list, my_list2)
print(f"My list is formed by: {my_list} and its lenght is {len(my_list)}")
print(['one','two','three',4,5])