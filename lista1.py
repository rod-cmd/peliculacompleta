
def contar_ocurrencias(lista, elemento_buscado): 
    contador = 0 # Inicializa el contador en 0  
    for elemento in lista: # Itera sobre cada elemento de la lista    
        if elemento == elemento_buscado: # Si el elemento es igual al elemento buscado
            contador += 1 # Incrementa el contador en 1
    return contador  # Retorna el contador  # Fin de la función      

mis_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
elemento_buscado = 10
resultado = contar_ocurrencias(mis_numeros, elemento_buscado) 
print (f"El elemento {elemento_buscado} aparece {resultado} veces en la lista.") 
