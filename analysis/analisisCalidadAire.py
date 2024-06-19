import pandas as pd

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando con dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=['comuna','ICA','fecha','ID'])
    dataFrameICA.to_csv('datosica.csv',index=False)
    print(dataFrameICA)
construirDataICA()