def nuevoTema(tema):
    print("\n=======", tema,"=======\n")


'''print("hola mundo python")
print("Operador division entera (10//3):",10//3)
print("Operador potencia(5**3):",5**3)  #operador'''
'''este es un comentario de varias lineas'''

'''print("======OPERADORES LOGICOS=======")
print("Operador and(True and False): ",True and False)'''

#Actividad imprimir tabla de la verdad de los operadores logicos.
print("===Operador and===")
print("true and true   ",True and True)
print("true and false  ",True and False)
print("False and True  ",False and True)
print("False and False ",False and False)
print("\n")
print("===OPERADOR OR===")
print("true or true   ",True or True)
print("true or false  ",True or False)
print("False or True  ",False or True)
print("False or False ",False or False)
print("\n")


print("============OPERADORES DE COMPARACION=========")
print("2>3",2>3)
print("2<=3",2<=3)
print("2<3",2<3)
print("2>=3",2>=3)
print("2==3",2==3)
print("2!=3",2!=3)

print("_________________________________________")


nuevoTema("variables")
variable1 = 18
_variable2= 20
variable3 = "juan"
dosPalabras = "hola"
dos_palabras = "hello"

print(variable1,_variable2,variable3,dos_palabras,dos_palabras)
a,b,c= 10,5,"palabra"

print("_________________________________________")


nuevoTema("enteros")
w=21
x=2342343242343
y=-123
z=0b00110011
h=0xffa

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))
print("_________________________________________")


nuevoTema("flotantes")
x=21.222
print(x,type(x))
y=0.234234
print(y, type(z))

print("_________________________________________")


nuevoTema("numeros complejos")
x= 46j
y= 12+45j
z= 2j

print(x,type(x))
print(y,type(y))
print(z,type(z))
print("_________________________________________")

nuevoTema("booleanos")
lis=[8]
print(lis,"es",bool(lis))
t=()
print(t, "ES",bool(t))
new= "hello"
print(new,"es",bool(new))
num=99
print(num,"es",bool(num))
comp=1+0j
print(comp,"es",bool(comp))
val=None
print(val,"es",bool(val))


print("_________________________________________")

nuevoTema("listas")#NO SON LISTAS
a=[10,25.5,"python lista"]
print(a)
print(a[0])

print("_________________________________________")

nuevoTema(tuple)
t=(25,"tupla",1+10j,3.1416)
print(t)
print(t[2])
print("t[0:2]",t[0:4])
