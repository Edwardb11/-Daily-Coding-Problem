#Spanish
#¡Buenos días! Aquí está el problema de codificación de la entrevista de hoy.
#Google preguntó recientemente este problema.
# Dada una lista de números y un número k, devuelva si dos números cualesquiera de la lista suman k.
#Por ejemplo, dado [10, 15, 3, 7] yk de 17, devuelve verdadero ya que 10 + 7 es 17.
#Bono: ¿Puedes hacer esto en una sola pasada?

#English
#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

def buscando(lista, k):
    for i in range(0, len(lista)):
        if k - lista[i] in lista:
            return True
    return False        
lista= [10, 15, 3, 7]
k = 17
print(buscando(lista, k))