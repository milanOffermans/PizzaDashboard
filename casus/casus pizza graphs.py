import pandas as pd 
from matplotlib import style
from search_by_name import fileHandler
from Diagram_components import Bar_diagram
from Diagram_components import Circel_diagram
from Diagram_components import Line_diagram
from Diagram_components import Wireframe_diagram
from sqlite_db import Database
from tkinter import *
from tkinter import ttk
import numpy as np

#filename =  'Data_Model_Pizza_Sales.xlsx'
#filePath = 'c:\\temp\\Data_Model_Pizza_Sales.xlsx'
#df = pd.read_excel(filePath)
style.use('ggplot')
def line():
    data =  Database.GetLineDiagramData()
    
    categories = [item["category"] for item in data]
    total = [item["total"] for item in data]

    Line_diagram.Line_diagram.Createline(categories,total)

#Bar graph
def bar():
    data =  Database.GetBarDiagramData()

    Bar_diagram.Bar_diagram.Createbar(data)

#Circle graph
def circle():
    data =  Database.GetCircleDiagramData()
    categories = [item["category"] for item in data]
    total = [item["total"] for item in data]

    Circel_diagram.Circel_diagram.CreateCirle(total,categories)

#wireframe
def wireframe():
    data =  Database.GetWireframeDiagramData()

    date = [item["order_date"] for item in data]
    name = [item["pizza_name"] for item in data]
    quantity = [item["pizza_size"] for item in data]
    for i in range(0 , len(quantity)):
        x = np.linspace(date, name, quantity)
        y = np.linspace(date, name, quantity)
        x, y = np.meshgrid(x, y)
        z = np.sin(np.sqrt(x**2 + y**2))

    Wireframe_diagram.Wireframe_diagram.CreateWireFrame(x,y,z)    

root = Tk()
root.title('Pizza Dashboard')
frm = ttk.Frame(root, padding=5)
root.geometry('300x100')
frm.grid()
ttk.Label(frm, text="Welcome!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=10)
ttk.Button(frm, text="Line diagram", command=line).grid(column=0, row=5)
ttk.Button(frm, text="Bar diagram", command=bar).grid(column=1, row=5)
ttk.Button(frm, text="Circel", command=circle).grid(column=0, row=8)
ttk.Button(frm, text="Wireframe", command=wireframe).grid(column=1, row=8)
root.mainloop()

#Line graph
