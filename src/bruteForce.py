import numpy as np
import math

def getRumus(pangkat):
    arrayKoefisien = []
    for i in range(pangkat + 1):
        koeefisien = math.comb(pangkat, i)
        arrayKoefisien.append(koeefisien)

    return arrayKoefisien

def getPointToDrawBruteForce(arrayTitikX,arrayTitikY,jumlahIterasi):
    koefisien = getRumus(len(arrayTitikX)-1)
    arrayTitikBezierX = []
    arrayTitikBezierY = []
    rangeValueT = np.linspace(0, 1, num=1+pow(2,jumlahIterasi))
    for valueT in rangeValueT:
        tempx = 0
        tempy = 0
        for j in range(len(arrayTitikX)):
            tempx = tempx + pow((1-valueT),len(koefisien)-1-j)*pow(valueT,j)*arrayTitikX[j]*koefisien[j]
            tempy = tempy + pow((1-valueT),len(koefisien)-1-j)*pow(valueT,j)*arrayTitikY[j]*koefisien[j]
        arrayTitikBezierX.append(tempx)
        arrayTitikBezierY.append(tempy)
    return zip(arrayTitikBezierX,arrayTitikBezierY)



