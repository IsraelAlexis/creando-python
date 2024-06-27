import random

def generarDatosICA():
    datosEncuesta=[]
    for i in range(2000):
        dato={}
        comuna=random.choice(['poblado:comuna 1','aranjuez:comuna 2','robledo:comuna 3','manrique:comuna 4','boston:comuna 5','estadio:comuna 6','candelaria:comuna 7','enciso:comuna 8','salvador:comuna 9','barrio trsite:comuna 10','laureles:comuna 11','floresta:comuna 12','san javier:comuna 13','chagualo:comuna 14','castilla:comuna 15','guayabal:comuna 16','sin','-','nan'])
        ica=random.randint(10,100)
        fecha=random.choice(['2024-06-23','2024-06-25','2024-01-30','2024-07-31'])  
        id=random.randint(1,50000)
        dato=[comuna,ica,fecha,id]
        datosEncuesta.append(dato)
    return (datosEncuesta)
   # print(datosEncuesta)
   

generarDatosICA()