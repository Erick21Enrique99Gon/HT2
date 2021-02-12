#Ejercicio 1
#Funcion de calculo de descuento
def descuento(precio,descuento):
    x=precio*descuento
    return precio-x
#Funcion de calculo de IVA
def impuestoIVA(precio):
    x=precio*0.12
    return precio+x
#Diccionario de carrito de compras
productos ={
    'producto1': [10,0.23],
    'producto2': [20,0.5],
    'producto3': [30,0.35],
    'producto4': [40,0.2],
}
#Funcion de aplicacion de calculos sobre 
def calculo (carito,operacion,tipo):
    Total = 0
    if tipo==0:
        for i in carito:
            Total = Total+operacion(carito[i][0],carito[i][1])
    else:
        for i in carito:
             Total =Total+ operacion(carito[i][0])
    print('Total es :')
    print(Total)         
#Calculo de descuento
calculo(productos,descuento,0)
#Calculo de IVA
calculo(productos,impuestoIVA,1)

#Ejercicio 2
#Funcion de elevar al cuadrado
def cuadrado(numero):
    return numero*numero
#Funcion de aplicacion a la lista
def proceso(funcion,numeros):
    cuadrado = []
    for i in numeros:
        cuadrado.append(funcion(i))
    return cuadrado 
#llamada a la Funcion
print(proceso(cuadrado,[1,2,3,4]))