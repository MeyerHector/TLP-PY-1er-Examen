import matplotlib.pyplot as plt
from punto2 import df, promedio_notas_por_estudiante

datos = promedio_notas_por_estudiante(df) # Obtengo el dataframe con la funcion anteriormente creada

def crear_grafico(datos):

    nombres = datos['nombre'] # Obtengo los nombres de los estudiantes y los promedios
    promedios = datos['promedio']

    plt.bar(nombres, promedios) # Creo el gráfico de barras

    # Personalizacion
    plt.xlabel('Estudiantes')
    plt.ylabel('Promedio de calificaciones')
    plt.title('Promedio de calificaciones por estudiante')

    plt.show() # Muestro el gráfico

crear_grafico(datos)