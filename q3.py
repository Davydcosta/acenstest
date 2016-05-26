a=80000
b=200000
cont=0
while a<=b:
    c=a*0.03
    d=b*0.0152
    a=a+c
    b=b+d
    cont+=1
print("Necessario %d anos" %cont)
print("Quantidade do pais A %d " %a)
print("Quantidade do pais B %d" %b)
