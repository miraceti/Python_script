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

#filter function : create a collection of element from an iterable if return ttrue
# filter(function, iterable)

store =[("shirt",20.00),("pants",25.00),("jacket",50.00),("socks",10.00)]

# function
age = lambda data: data[1] > 10.00

# filter
storef=list(filter(age, store))

for i in storef:
    print(i)

import functools  
# reduce function : reduce(function, iterable)
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,: x * y, factorial)
print("result : ",result)

# list comprehension
# create a new list with less syntax
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditions]
# list = [expression if/else for item in iterable]

squares =[]
for i in range(1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students = [i for i in students if i >= 60]
print(passed_students)

passed_students = [i  if i >= 60 else "Echec" for i in students]
print(passed_students)

# dictionary comprehension
# dict = {key: expression for (k,v) in iter}
# dict = {key: expression for (k,v) in iter if cond}
# dict = {key: if/else for (k,v) in iter}
# dict = {key: function(v) for (k,v) in iter}
cities_in_f = {'ny':32, "boston":75, "los angeles": 100, 'chicago':50}
cities_in_c = {k: round(((v-32)*(5/9))) for (k,v) in cities_in_f.items()}
print(cities_in_c)

weather ={'ny':'snowing', 'boston':'sunny',"los angeles":"sunny", "chicago":"cloudy"}
sunny_weather = {k: v for (k,v) in weather.items() if v == "sunny"}
print(sunny_weather)
sunny_weather_k = {k for (k,v) in weather.items() if v == "sunny"}
print(sunny_weather_k)
sunny_weather_v = {v for (k,v) in weather.items() if v == "sunny"}
print(sunny_weather_v)

cities = {'ny':32, "boston":75, "los angeles": 100, 'chicago':50}
desc_cities = {k: ("Hot!" if v >= 40 else "Cold") for (k,v) in cities.items()}
print(desc_cities)

cities2 = {'ny':32, "boston":75, "los angeles": 100, 'chicago':50}
def check_temp(v):
    if v >= 70:
       return "hot"
    elif 69 >= v >= 40:
        return "warm"
    else:
       return  "cold"
desc_cities2 = {k: check_temp(v) for (k,v) in cities2.items()}
print(desc_cities2)

# zip (*iter) : agregate elements from 2 or more iter (list, tuple, set) and create a zip object
usernames =["dude","bro","mister"]
passwords=("p@ssword","abc123","guest")
users =zip(usernames,passwords)
print(users)
for i in users:
    print(i)
    
usersl = list(zip(usernames,passwords))
print(usersl)

usersd = dict(zip(usernames,passwords))
print(usersd)
for k,v in usersd.items():
    print(k+' : '+v)

login_date = ["1/1/2021","1/2/2021","1/3/2021"]
usersld = zip(usernames, passwords, login_date)
for i in usersld :
    print(i)
    
# time
import time

print(time.ctime(0)) #01/01/1970
print(time.time())#nb second from epoch 

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
# strftime
local_time1 = time.strftime("%d/%m/%y",time_object)
print(local_time1)
local_time2 = time.strftime("%d/%m/%Y",time_object)
print(local_time2)
local_time3 = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time3)

# strptime
time_string="20 April, 2020"
time_object1 = time.strptime(time_string, "%d %B, %Y")
print(time_object1)

# asctime
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string2 = time.asctime(time_tuple)
print(time_string2)

