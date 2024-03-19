import tkinter as tk
import tkinter.messagebox as messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import dnc
import bruteForce

def drawCurve(arrayTitikX, arrayTitikY, arrayTitikBezierX, arrayTitikBezierY, choiche):
    global canvas, widget
    if widget is not None:
        widget.destroy()

    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    if choiche == 0:
        arrayTitikBezierX = list(arrayTitikBezierX)
        arrayTitikBezierX.insert(0,arrayTitikX[0])
        arrayTitikBezierX.append(arrayTitikX[len(arrayTitikX)-1])
        arrayTitikBezierX = tuple(arrayTitikBezierX)
        arrayTitikBezierY = list(arrayTitikBezierY)
        arrayTitikBezierY.insert(0,arrayTitikY[0])
        arrayTitikBezierY.append(arrayTitikY[len(arrayTitikY)-1])
        arrayTitikBezierY = tuple(arrayTitikBezierY)

    ax.plot(arrayTitikX, arrayTitikY, marker='o', label="Titik kontrol")
    ax.plot(arrayTitikBezierX, arrayTitikBezierY, marker='o', label="Bezier curve")
    ax.legend()
    
    if choiche == 0:
        ax.set_title("Divide and Conquer")
    else:
        ax.set_title("Brute Force")

    canvas = FigureCanvasTkAgg(fig, master=root)  
    canvas.draw()
    widget = canvas.get_tk_widget()
    widget.pack()
       
def button(choice):
    jumlahTitik = int(inputN.get())
    jumlahIterasi = int(inputT.get())
    arrayTitikX = [float(i) for i in inputX.get().split()]
    arrayTitikY = [float(i) for i in inputY.get().split()]

    if len(arrayTitikX) != jumlahTitik or len(arrayTitikY) != jumlahTitik:
        messagebox.showinfo("Warning","Maaf jumlah titik dan jumlah x atau y tidak sama.")
        return
    else:
        startTime = time.time()
        if choice == 0:
            arrayTitikBezierXY = dnc.getPointToDrawDivideAndConquer(arrayTitikX, arrayTitikY, jumlahIterasi)
        else:
            arrayTitikBezierXY = bruteForce.getPointToDrawBruteForce(arrayTitikX, arrayTitikY, jumlahIterasi)
        endTime = time.time()
        executionTime = endTime - startTime

        executionTimeLabel.config(text=f"Waktu eksekusi: {executionTime} detik")
        arrayTitikBezierX, arrayTitikBezierY = zip(*arrayTitikBezierXY)
        drawCurve(arrayTitikX, arrayTitikY, arrayTitikBezierX, arrayTitikBezierY, choice)

canvas = None
widget = None

root = tk.Tk()

textInputN = tk.Label(root, text="Masukkan jumlah titik: ")
textInputN.pack()
inputN = tk.Entry(root)
inputN.pack()

textInputX = tk.Label(root, text="Masukkan nilai x (pisahkan dengan spasi): ")
textInputX.pack()
inputX = tk.Entry(root)
inputX.pack()

textInputY = tk.Label(root, text="Masukkan nilai y (pisahkan dengan spasi): ")
textInputY.pack()
inputY = tk.Entry(root)
inputY.pack()

textInputT = tk.Label(root, text="Masukkan jumlah iterasi yang ada ingin kan: ")
textInputT.pack()
inputT = tk.Entry(root)
inputT.pack()

buttonFrame = tk.Frame(root)
buttonFrame.pack()
divideAndConquerButton = tk.Button(buttonFrame, text="Divide and Conquer", command=lambda: button(0))
divideAndConquerButton.grid(row=0, column=0)
bruteForceButton = tk.Button(buttonFrame, text="Brute Force", command=lambda: button(1))
bruteForceButton.grid(row=0, column=1)

executionTimeLabel = tk.Label(root)
executionTimeLabel.pack()

root.mainloop()