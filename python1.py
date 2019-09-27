# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:23:40 2019

@author: RufinoS
"""

a = "Rufino Salgado"
b = "Hello"
words = [a, b]
c = " ".join(words)

d = 23
e = 45.3

list1 = [a, b, c, d, e]

f = 65

list1.append(f)

list1.insert(0,"list")

print(list1)

tuple1 = (a, b, c, d, e, f)

dict1 = {a:b, c:d, e:f}

print(tuple1)

print(dict1)

list2 = []

for key in dict1.keys():
    print(dict1[key], end=" ")
    
print(list1)
del(list1[0])
print(list1)

print(list1)
inp = input("enter a name: ")
list1.append(inp)
print(list1)

with open("textfile.txt", "w") as f:
    for item in list1:
        f.write(str(item))
        
with open("textfile.txt", "r") as f:
    print(f.read())
    
with open("textfile.txt", "a") as f:
    f.write("\n")
    for item in list1:
        f.write(str(item) + " ")
        
with open("textfile.txt", "r") as f:
    print(f.read())

def add(num1, num2):
    return num1 + num2

inp = input("Enter a number: ")
num1 = int(inp)
inp = input("Enter another number: ")
num2 = int(inp)

fun = add
print(add(num1, num2))
print(fun(num1, num2))

class Fish:
    name = ""
    species = ""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def swim(self):
        print(self.name, " is swimming")
        
    def eat(self):
        print(self.name, " is eating")
        
fish = Fish("Jerry", "goldfish")

fish.eat()

#copy a list
numbers = list(range(1, 23))
numbers
newNumbers = [num for num in numbers]
newNumbers
newNumbers = [num for num in numbers if (num % 2 == 0)]
 