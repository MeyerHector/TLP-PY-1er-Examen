import pandas as pd
from calificaciones import calificaciones

df = pd.DataFrame(calificaciones, columns=['nombre', 'matematicas', 'ciencias', 'historia'])
# print(df)
def calcular_promedio(df, materia):
    df_promedio = pd.DataFrame(df[f'{materia}'])
    df_promedio['Fi'] = df_promedio[f'{materia}'].cumsum()
    promedio = df_promedio['Fi'][12] / 12 

    return f'El promedio de {materia} es {promedio}'
# print(calcular_promedio(df, 'matematicas'))
# print(calcular_promedio(df, 'ciencias'))
# print(calcular_promedio(df, 'historia'))

def encontrar_calf_mas_altas(df, materia):
    order = pd.DataFrame(df[['nombre', f'{materia}']])
    order.sort_values(by=f'{materia}', ascending=False, inplace=True)
    return 'la calificacion mas alta es de', order.iloc[0]['nombre'], 'y es de ', order.iloc[0][f'{materia}']

# print(encontrar_calf_mas_altas(df, 'matematicas'))
# print(encontrar_calf_mas_altas(df, 'ciencias'))
# print(encontrar_calf_mas_altas(df, 'historia'))


def porcentaje_aprobados(df, materia):
    aprobados = df[df[materia] >= 60]
    porcentaje = (len(aprobados) / len(df)) * 100
    return f'El porcentaje de estudiantes que aprobaron {materia} es {porcentaje}%'

# print(porcentaje_aprobados(df, 'matematicas'))
# print(porcentaje_aprobados(df, 'ciencias'))
# print(porcentaje_aprobados(df, 'historia'))


def cantidad_notas(df, materia):
    print('hola')
