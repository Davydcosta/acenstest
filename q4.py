import random
lista1=[]
lista2=[]
lista3=[]
a=0
b=0
c=0
while a<10:
    lista1.append(random.randint(1,100))
    a+=1
print lista1

while b<10:
    lista2.append(random.randint(1,100))
    b+=1
print lista2

while c<10:
    lista3.append(lista1[c])
    lista3.append(lista2[c])
    c+=1
print lista3
