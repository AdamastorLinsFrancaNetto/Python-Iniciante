import array


def calcAreaTriangulo(base, altura):
    return (base*altura)/2
print("A área do triângulo é:",calcAreaTriangulo(3,10))

def calcAreaCirculo(raio):
    return 3.14*pow(raio,2)
print("A área do circulo é:",calcAreaCirculo(5))

def calcAreaQuadrado(lado):
    return lado*lado
print("A área do quadrado é:",calcAreaQuadrado(4))

def calcAreaTerreno(lado,raio,base,altura):
    return calcAreaQuadrado(lado) + 2*calcAreaCirculo(raio) + calcAreaTriangulo(base, altura)
    #return (lado*lado)+(3.14*pow(raio,2))+((base*altura)/2)
print("A área do terreno é: %.2f"%calcAreaTerreno(5.7,3.5,4,3))

def calcMedias(nota1,nota2,nota3,letra):
    if letra == "a":
        return (nota1+nota2+nota3)/3
    if letra == "p":
        return ((nota1*5)+(nota2*3)+(nota3*2))/(5+3+2)
    if letra == "h":
        return 3/(1/nota1)+(1/nota2)+(1/nota3)
print("O valor da área é:",calcMedias(10,10,10,"a"))

def calcPagamentos(qntHoras, valorHoras):
    if qntHoras <= 40:
        return qntHoras * valorHoras
    else:
        return (40 * valorHoras) + ((qntHoras - 40)*(1.5 * valorHoras))
print("O valor do pagamento é: R$",calcPagamentos(50,10))

def calcPotencia(primValor, segValor):
    return  pow(primValor,segValor)
print("O resultado da ponteciação é:",calcPotencia(2,3))
print("O resultado da ponteciação é:",calcPotencia(3,2))
print("O resultado da ponteciação é:",calcPotencia(3,-2))
print("O resultado da ponteciação é:",calcPotencia(3,0))
print("O resultado da ponteciação é:",calcPotencia(0,2))












