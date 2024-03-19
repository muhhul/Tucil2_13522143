def getMiddlePoint(arrayTitikX,arrayTitikY,jumlahIterasi):
    arrayMiddleX = []
    arrayMiddleY = []
    x = []
    y = []

    if len(arrayTitikX)==2:
        tempX = (arrayTitikX[0]+arrayTitikX[1])/2
        tempY = (arrayTitikY[0]+arrayTitikY[1])/2
        arrayMiddleX.append(tempX)
        arrayMiddleY.append(tempY)

        return zip(arrayMiddleX,arrayMiddleY)
    elif len(arrayTitikX)>2:
        for i in range(len(arrayTitikX)-1):
            tempX = (arrayTitikX[i]+arrayTitikX[i+1])/2
            tempY = (arrayTitikY[i]+arrayTitikY[i+1])/2
            arrayMiddleX.append(tempX)
            arrayMiddleY.append(tempY)
            if i == 0 or i == len(arrayTitikX)-2:
                x.append(tempX)
                y.append(tempY)
        arrayMiddleX, arrayMiddleY = zip(*getMiddlePoint(arrayMiddleX,arrayMiddleY,jumlahIterasi))
        x = x[:1] + list(arrayMiddleX) + x[1:]
        y = y[:1] + list(arrayMiddleY) + y[1:]

        return zip(x,y)
    
def getPointToDrawDivideAndConquer(arrayTitikX,arrayTitikY,jumlahIterasi):
    x = []
    y = []
    if jumlahIterasi > 1:
        arrayMiddleX, arrayMiddleY = zip(*getMiddlePoint(arrayTitikX,arrayTitikY,jumlahIterasi))
        jumlahIterasi = jumlahIterasi - 1

        arrayMiddleX = list(arrayMiddleX)
        arrayMiddleY = list(arrayMiddleY)
        arrayLeftX = []
        arrayLeftY = []
        newSizeArray = int((len(arrayMiddleX)+1)/2)
        for i in range(newSizeArray):
            arrayLeftX.append(arrayMiddleX[i])
            arrayLeftY.append(arrayMiddleY[i])

        arrayRightX = []
        arrayRightY = []
        for i in range(newSizeArray):
            arrayRightX.append(arrayMiddleX[i+int((len(x)/2))+int(len(arrayMiddleX)/2)])
            arrayRightY.append(arrayMiddleY[i+int((len(x)/2))+int(len(arrayMiddleX)/2)])
        
        arrayLeftX.insert(0,arrayTitikX[0])
        arrayLeftY.insert(0,arrayTitikY[0])
        arrayRightX.append(arrayTitikX[len(arrayTitikX)-1])
        arrayRightY.append(arrayTitikY[len(arrayTitikY)-1])
        arrayLeftX,arrayLeftY = zip(*getPointToDrawDivideAndConquer(arrayLeftX,arrayLeftY,jumlahIterasi))
        arrayRightX,arrayRightY = zip(*getPointToDrawDivideAndConquer(arrayRightX,arrayRightY,jumlahIterasi))

        x.extend(arrayLeftX)
        y.extend(arrayLeftY)
        x.append(arrayMiddleX[int(len(arrayMiddleX)/2)])
        y.append(arrayMiddleY[int(len(arrayMiddleY)/2)])
        x.extend(arrayRightX)
        y.extend(arrayRightY)
        return zip(x,y)
    
    elif jumlahIterasi == 1 :
        arrayMiddleX, arrayMiddleY = zip(*getMiddlePoint(arrayTitikX,arrayTitikY,jumlahIterasi))
        x.append(arrayMiddleX[int(len(arrayMiddleX)/2)])
        y.append(arrayMiddleY[int(len(arrayMiddleY)/2)])
        return zip(x,y)
    
    else:
        arrayBezierX = []
        arrayBezierY = []
        arrayBezierX.append(arrayTitikX[0])
        arrayBezierY.append(arrayTitikY[0])

        arrayBezierX.append(arrayTitikX[len(arrayTitikX)-1])
        arrayBezierY.append(arrayTitikY[len(arrayTitikY)-1])

        return zip(arrayBezierX,arrayBezierY)
