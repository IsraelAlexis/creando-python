import pandas as pd

from generators.generadordecibelios import generarDatosRuido

def construirDataRuido():
    #creando con dataFrame
    datosRuido=generarDatosRuido()
    dataFrameRuido=pd.DataFrame(datosRuido,columns=['id','nivelRuido','comuna'])
    dataFrameRuido.to_csv('datosRuido.csv',index=False)
    print(dataFrameRuido)
    
construirDataRuido()
