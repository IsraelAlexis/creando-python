import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando con dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=['comuna','ICA','fecha','ID'])
    dataFrameICA.to_csv('datosica.csv',index=False)
    print(dataFrameICA)
    
    #generando grafica de los datos por comuna
   # datosOrdenadosPorComuna=dataFrameICA.groupby('comuna')['ICA'].mean()
   # plt.figure(figsize=(20,20))
   # datosOrdenadosPorComuna.plot(kind='bar',color='green')
   # plt.show()

construirDataICA()