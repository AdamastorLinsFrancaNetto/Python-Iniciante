#Implemente um script Python para mostrar os 20 primeiros números impares.

#while
cont=0
while cont <= 20:
   if cont%2 !=0:
       print(cont)
   cont+=1
print("")

#for
for i in range (1,20,1):
    if i%2!=0:
        print(i)