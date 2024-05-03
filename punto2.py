import pandas as pd
from calificaciones import calificaciones

df = pd.DataFrame(calificaciones, columns=['nombre', 'matematicas', 'ciencias', 'historia'])
# print(df)
def calcular_promedio(df, materia):

    df_promedio = pd.DataFrame(df[f'{materia}']) # Genero un df con el nombre de la materia que recibo como parametro
    
    df_promedio['Fi'] = df_promedio[f'{materia}'].cumsum() # Agrego una columna de frecuencia simple acumulada para sumar la cantidad de notas
    
    promedio = df_promedio['Fi'].iloc[-1] / len(df_promedio['Fi']) # Divido la Fi por la cantidad de notas y obtengo el promedio

    return f'El promedio de {materia} es {promedio}' # Devuelvo con su mensaje correspondiente

# print(calcular_promedio(df, 'matematicas'))
# print(calcular_promedio(df, 'ciencias'))
# print(calcular_promedio(df, 'historia'))

def encontrar_calf_mas_altas(df, materia):

    order = pd.DataFrame(df[['nombre', f'{materia}']]) # Creo un df con el nombre (del estudiante) y la materia que se ingrese por parametros
    
    order.sort_values(by=f'{materia}', ascending=False) # utilizo la funcion sort_values(), pasandole como parametro la materia, en orden descendiente, por lo que la nota mayor estara en la posicion 0
    nombre_alumno = order.iloc[0]['nombre'] # Accedo a esa posicion y obtengo el nombre
    nota_alumno = order.iloc[0][f'{materia}'] # Accedo a la misma posicion y obtengo la nota

    return f'la calificacion mas alta de {materia} es de {nombre_alumno} y es de {nota_alumno}' # devuelvo mensaje con las variables correspondientes

# print(encontrar_calf_mas_altas(df, 'matematicas'))
# print(encontrar_calf_mas_altas(df, 'ciencias'))
# print(encontrar_calf_mas_altas(df, 'historia'))


def porcentaje_aprobados(df, materia):

    aprobados = df[df[materia] >= 60] # guardo en la variable aprobados solamente los datos del df en la cual la nota de la materia sea mayor igual a 60

    porcentaje = (len(aprobados) / len(df)) * 100 # saco el porcentaje dividiendo la cantidad de aprobados por la cantidad de registros que hay en notas, y eso lo multiplico por 100
    
    return f'El porcentaje de estudiantes que aprobaron {materia} es {porcentaje}%' # devuelvo mensaje correspondiente

# print(porcentaje_aprobados(df, 'matematicas'))
# print(porcentaje_aprobados(df, 'ciencias'))
# print(porcentaje_aprobados(df, 'historia'))


def promedio_notas_por_estudiante(df):
    # Creo un df que tenga los mismos datos del original pero agregandole otra columna llamada promedio
    df_promedio_estudiantes = pd.DataFrame(df, columns=['nombre', 'matematicas', 'ciencias', 'historia', 'promedio'])
    # Sumo las tres notas del mismo registro y lo guardo en promedio
    df_promedio_estudiantes['promedio'] = df_promedio_estudiantes['matematicas'] + df_promedio_estudiantes['ciencias'] + df_promedio_estudiantes['historia']
    # Y finalmente divido promedio por 3 para obtener el promedio final de nota por estudiante
    df_promedio_estudiantes['promedio'] = (df_promedio_estudiantes['promedio'] / 3).round()

    # Borro las columnas que ya no necesito con el metodo drop() pasandole las columnas que quiero que elimine, el axis en uno para que borre la columna por completo y no solamente los registros y por ultimo le paso inplace=True para que modifique el df original
    df_promedio_estudiantes.drop(labels=['matematicas', 'ciencias', 'historia'], axis=1, inplace=True)

    return df_promedio_estudiantes


# print(promedio_notas_por_estudiante(df))