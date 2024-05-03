
def eliminar_duplicados(datos_duplicados):
    if not datos_duplicados: # Verifico que se hayan mandado datos
        return 'No se encontraron datos'
    elif len(datos_duplicados) == 1: # Si es un solo dato la devuelvo 
        return datos_duplicados
    
    lista_limpia = list(set(datos_duplicados)) # Los conjuntos no pueden tener datos duplicados, creo uno y le paso la lista duplicada, luego lo convierto a lista con list() y la retorno
    
    return lista_limpia

print(eliminar_duplicados([1, 1, 2, 3, 4, 5, 5, 6, 7]))