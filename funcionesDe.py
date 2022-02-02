from decimal import Rounded
import random
import statistics as stats
import calendar
import datetime




def operaciones(num1,num2):   
   print("suma")
   suma=num1+num2
   print(suma)
   print("resta")
   resta=num1-num2
   print(resta)
   print("Multiplicación")
   multi=num1*num2
   print(multi)
   print("División")
   divi=num1/num2
   print(divi)


def aleatorio():
   aleatorio=random.randint(1,120)
   return aleatorio

def bucles():
    for i in range(1,11):
        print(i)

        
def series():
    suma=0
    for i in range(1,11):
        suma+=i
    return suma



def unirListas():
    una=list(range(1,11))
    dos=list(range(11,21))
    print("Lista1:")
    print(una)
    print("Lista2:")
    print(dos)
    print("Junta:")
    completa=una+dos
    return completa



def mediaDosnumeros(num1, num2):
    numeros=[num1,num2]
    print(stats.mean(numeros))
    


     

def medianNumeros():
    canti = 0
    numeros=[]
    while (canti < 1):
            canti = int(input("Ingrese la cantidad de números a calcular: "))
            for i in range(canti):
                numero= float(input('ingrese un número:'))
                numeros.append(numero)
            print("Media:",stats.mean(numeros))
        
def adivinaNumero():
    print("Tienes un total de 4 intentos. Usalos sabiamente")
    intentos=0
    aleatorio=random.randint(1,100)
    numero=int(input("ingrese un número :"))
    while True:
       intentos+=1
       if numero==aleatorio:
                print("Bien hecho, has adivinado el número secreto:", aleatorio)
                break
       if numero>aleatorio:
           print("Intenta con uno menor :) ")
           numero=int(input("ingrese un número"))
       else:
           print("Intenta con uno mayor :) ")    
           numero=int(input("ingrese un número :"))
       if intentos==3:
           print("Has agotado tus 4 intentos, el número era", aleatorio)
           break
       
def  imc(h,w):
    print("Composición corporal:")
    imc=w/pow(h,2)
    print(round(imc,2))
    if imc<18.5:
        print ("insuficiencia ponderal")
    if imc>=18.5 and imc<= 24.9:
       print ("Normal")
    if imc>=25.0 and imc<=29.9:
       print ("w superior al normal")
    if imc>=300:
        print ("obesidad")
     

    

def calendario(): 
    month = datetime.date.today().month
    year = datetime.date.today().year
    print (calendar.month(year,month))
    
        
def anagrama(texto1,texto2):
   if sorted(texto1)==sorted(texto2):
       print(texto1, "es un anagrama de ", texto2)
   else:
       print(texto1, "no es un anagrama de ", texto2)

def maximoMinimo():
    numeros=[]
    for i in range(11):
        aleatorios=random.randrange(1, 100)
        numeros.append(aleatorios)
    print("Numeros generados", numeros)    
    print("El máximo es", max(numeros),"\n", "El mínimo es", min(numeros))
    
def pitagoras():
    
    for catetoA in range(1,101):
      for catetoB in range(catetoA,101):
        hipotenusa=(catetoA**2+catetoB**2) **.5
        if hipotenusa == int(hipotenusa):
            print("A:",catetoA, "B:",catetoB,"H:", int(hipotenusa))
            
def acumulado():
    listcuadrados=[]
    listcubos=[]
    numeros=[]
    for i in range(1, 11):
        cuadrados=i**2
        cubos=i**3
        numeros.append(i)
        listcuadrados.append(cuadrados)
        listcubos.append(cubos)
        print("Numero:", i ,"Cuadrado", cuadrados ,"Cubos:", cubos)
    print("Totales:")
    print( "Numeros:", sum(numeros) ,"Cuadrados:", sum(listcuadrados), "Cubos:", sum(listcubos))
    
    
def aleatoriosExcepciones():
    numeros = []
    for i in range(10):
        aleatorio = random.randrange(100,131,2)
        if aleatorio not in (110,120):
            numeros.append(aleatorio)
    print(numeros)
    
def generarPalabras():
    palabras=[]
    abecedario=["a","b", "c,""d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]    
    for i in range(0,11):
        palabra_actual=[]
        for j in range(4):
            palabra_actual.append(abecedario[random.randint(0,24)])
        palabras.append(",".join(palabra_actual))
    print("Palabras generadas en forma aleatoria")
    print(palabras)
    print("Palabras generadas en orden alfabético")
    print(sorted(palabras))
    
    
def finobacci(cantiNum):
    n1=0
    n2=1
    for i in range(cantiNum-1):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
def dicionarios(numero):
   meses=[
     {
        "numero": 1,
        "mes": "enero",
        "dias": 31,
    },
    {
        "numero": 2,
        "mes": "febrero",
        "dias": 28,

    },
     {
        "numero": 3,
        "mes": "marzo",
        "dias": 31,

    },
      
     {
        "numero": 4,
        "mes": "abril",
        "dias": 30,

    },
     {
        "numero": 5,
        "mes": "mayo",
        "dias": 31,

    },
     {
        "numero": 6,
        "mes": "junio",
        "dias": 30,

    },
     {
        "numero": 7,
        "mes": "junio",
        "dias": 30,

    },
     {
        "numero": 8,
        "mes": "agosto",
        "dias": 31,

    },
     {
        "numero": 9,
        "mes": "septiembre",
        "dias": 30,

    },
      {
        "numero": 10,
        "mes": "octubre",
        "dias": 31,

    },
     {
        "numero": 11,
        "mes": "Noviembre",
        "dias": 30,

    },  
     {
        "numero": 12,
        "mes": "Diciembre",
        "dias": 31,

    }, 
    ] 
   mes=meses[numero-1]["mes"]
   dia=meses[numero-1]["dias"]
   print("Mes:", mes, "#días:", dia)
    


    
def tuplas():
    estaciones=("invierno","otoño", "verano", "primavera")
    print("Tupla Estaciones")
    print(estaciones)
    print("Elementos:")
    for i in estaciones:
        print(i, end="  ")
    print()
    longitud=len(estaciones)
    print("La longitud de la tupla es:", longitud)
    
