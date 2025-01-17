import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Creo una ventana oculta de tkinter
Tk().withdraw()

#Abro la ventana del explorador de archivos donde puedo seleccionar el documento CSV
ruta_archivo = askopenfilename(
    title="Selecciona el archivo CSV",
    filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")]
)

#Variables
#Cambiamos el valor de columna de acuerdo a la columna que esperamos analizar
columnaAnalisis = "LumNumSer"

#Validacion de que el usuario si selecciono el archivo
if ruta_archivo:
    print(f"Archivo seleccionado: {ruta_archivo}")
    
    
    #Lectura del archivo CSV con pandas
    csv = pd.read_csv(ruta_archivo, delimiter=";")
    if columnaAnalisis in csv.columns:
        columna = csv[columnaAnalisis]
        if not columna.empty:
            print(f"La columna que vas a manejar es: {columna.name} y tiene los siguientes valores iniciales \n{columna.head()}")
        else:
            print("La columna no posee valores.")
        
        #Si todo sale bien hasta este punto procederemos a verificar en que parte de la columna existen valores repetidos
        valoresDuplicados = columna[columna.duplicated()].unique()
        
        if len(valoresDuplicados) > 0:
            print(f"Valores duplicados encontrados: {valoresDuplicados}")
        else:
            print("No se encontraron valores duplicados.")
        
        #Si hay duplicados es de suma importancia saber la concurrencia del error
        conteoValores = columna.value_counts()
        conteoDuplicados = conteoValores[conteoValores > 1]
        if not conteoDuplicados.empty:
            print("\nConteo de cada valor en la columna:")
            print(conteoDuplicados)
            frecuenciaDuplicado = conteoDuplicados.value_counts()
            print("\nFrecuencia de repeticiones:")
            print(frecuenciaDuplicado)

    else:
        print("No existe la columna que esperas analizar")
else:
    print("No se ha seleccionado ningun archivo.")
    