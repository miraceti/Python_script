#encoding: utf-8

website1 ="gttp://google.com"
website2 = "htpp://wikipedia.com"

slice = slice(7, -4)

print(slice)

print(website1[slice])
print(website2[slice])

for i in range (10):
    print(i)
#par defaut print afficvhe un \n a la fin mais on peut changer le caractère de fin par "end="
for i in range (10):
    print(i, end="")

# list 2dlist 3 et plus
util1 = ["dos","linux","win","mac"]

# tuple
util2 = ("dos","linux","win","mac",2,False)

#set    
util3 = {"dos","linux","win","mac"}

# dictionary
util4 = {1:"dos",2:"linux",3:"win",4:"mac"}

# fonction imbriquée
# print(round(abs(float(input("entrez un nombre positif : ")))))

print()
print(20*"*")
print("*args")
print(20*"*")
# *args
def add(*args):
    sum = 0
    print(args)
    for i in args:
        sum += i
    return sum

print("a1",add(1,2,3,4,5))
print("a2",add(1,3))

print()
print(20*"*")
print("**kwargs")
print(20*"*")
def hello(**kwargs):
    print("hello " + kwargs['first']+ " " + kwargs['last'])
    print(kwargs)
    print("hello",end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
        
        
hello (title="Mr ", first="Bro", middle="Dude", last="Code")

print()
print(20*"*")
print("str.format()")
print(20*"*")

#ajout 10 espaces après
name = "Bro"
print("Hello, my name is -{}-".format(name))
print("Hello, my name is -{:10}-".format(name))
# ou 10 avant
print("Hello, my name is -{:>10}-".format(name))
# ou centrer
print("Hello, my name is -{:^10}-".format(name))


number = 1000

print("the number is {:.3f}".format(number))
print("the number is {:,}".format(number))
print("the number is {:b}".format(number))
print("the number is {:o}".format(number))
print("the number is {:X}".format(number))
print("the number is {:E}".format(number))

# 2 decimales
pi=3.14159
print("the number is {:.2f}".format(pi))
# 1 decimale
print("the number is {:.1f}".format(pi))


print()
print(20*"*")
print("os")
print(20*"*")
import os

path = "D:/eric/python/perso/csv/test.csv"
if os.path.exists(path):
    print("fichier existe")
    if os.path.isfile(path):
        print("c'est bien un fichier")
    elif os.path.isdir(path):
        print("c'est bien un repertoire")    
else:
    print("fichier n'existe pas")
    
    
print()
print(20*"*")
print("file")
print(20*"*")
with open(path) as file:
    print(file)
    print(file.read())
# le fichier est automatiquement fermé
# on test si lle fichier est bien fermé
print(file.closed)

import shutil
import sys
# copyfile() : copies content of a file
# copy()     : copyfile + permission mode + destination paut etre un dossier
# copy2()   : copy + copy metadata (times modification/creation)
shutil.copyfile('README.md', 'D:/eric/python/perso/csv/R2.md')# copyfile(source,destination)

source="README.md"
destination="D:/eric/python/perso/csv/R1.md"

# pour afficher les caractères accentués dans la console
sys.stdout.reconfigure(encoding='utf-8')
# le fichier ou le dossier est déplacé
try:
    if os.path.exists(destination):
        print("le fichier existe déja dans le repertoire destination")
    else:
        os.replace(source, destination)
        # os.remove(file)#pour effacer un fichier
        # shutil.rmtree(dossier)#pour effacer un dossier non vide
        # os.rmdir(dossier_vide)#pour effacer un dossier  vide
        print(source+ " a été déplacé")
except FileNotFoundError:
    print("le fichier source n'existe pas")
    
# "list des modules"
# print(help("modules"))

#appel sequentiel de methode
#fonctionne uniquement si les méthode de classe retourne self
# car= Car()
# car.turn_on().drive()
# ou 
# en utilisant le caratere de line continuation
# car.turn_on()\
#    .drive()

#la fonction super()   : acces aux fonctions de la classe parente (tempory object)
# super().__init__(length,width)   si dans la classe parent on a la fonction __init__(self,length,width)

#  walrus  :=
# version sans walrus
print(happy := True)
# exemple
# foods = list()
# while True :
#     food = input("quel nourriture aimes tu ? : ")
#     if food == "quit":
#         break
#     foods.append(food)   
# print(foods) 

# # version avec walrus
# foods = list()
# while food := input("quel nourriture aimes tu ? :") != "quit":
#     print(food)
#     foods.append(food)
# print(foods)

# affecter une fonction a une variable
say = print
say("ceci est un print avec say :)")

print()
print(20*"*")
print("lambda")
print(20*"*")
# lambda parameter:expression
double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name +" "+last_name
age_check = lambda age: True if age >= 18 else False
print(age_check(18))
print((lambda x: x * 2)(5))

students = [("un","a",12),("deux","b",54),("trois","d",32),("quatre","c",12),("cinq","e",24)]
grade1 = lambda grades:grades[1] #tri par la seconde colonne donc abcde
grade2 = lambda grades:grades[2] #tri par la troisieme colonne donc  de nombre
students.sort(key=grade2, reverse=True)

for i in students:
    print(i)
    
# map(function, iterable)    # 
store =[("shirt",20.00),("pants",25.00),("jacket",50.00),("socks",10.00)]

to_euros = lambda data:  (data[0],data[1]*0.82)
to_dollars = lambda data:  (data[0],data[1]/0.82)

store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars,store))
print(store)
print(store_euros)
print(store_dollars)