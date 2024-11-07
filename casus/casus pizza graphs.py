# Uitleg van wat de code doet:

# Deze code creëert een GUI (grafische interface) waarin je verschillende grafieken kunt openen, 
# zoals een lijndiagram, staafdiagram, cirkeldiagram en wireframe-diagram. Elk diagram gebruikt 
# data uit een database die via een aparte functie wordt opgehaald. Met de knoppen in de GUI 
# kun je elk diagram afzonderlijk openen.


# Importeer de pandas-bibliotheek om makkelijk met data in tabellen te werken, bijvoorbeeld uit een Excel-bestand.
import pandas as pd 

# Importeer de stijlopties van matplotlib voor het maken van grafieken.
from matplotlib import style

# Importeer de fileHandler-klasse uit het bestand 'search_by_name' om bestanden te zoeken.
from search_by_name import fileHandler

# Importeer diagramcomponenten die grafieken kunnen maken: staaf-, cirkel-, lijn- en wireframe-diagrammen.
from Diagram_components import Bar_diagram
from Diagram_components import Circel_diagram
from Diagram_components import Line_diagram
from Diagram_components import Wireframe_diagram

# Importeer de Database-klasse om data uit een database op te halen.
from sqlite_db import Database

# Importeer tkinter om een grafische gebruikersinterface (GUI) te maken.
from tkinter import *
from tkinter import ttk

# Importeer numpy voor wiskundige bewerkingen, vooral handig bij het maken van wireframes.
import numpy as np

# Definieer de naam van het Excel-bestand waarin onze data staat.
filename = 'Data_Model_Pizza_Sales.xlsx'
#filePath = 'c:\\temp\\Data_Model_Pizza_Sales.xlsx'  # Optionele bestandslocatie
#df = pd.read_excel(filePath)  # Lees de Excel-data in een pandas DataFrame

# Stel de stijl voor de grafieken in op 'ggplot' voor een mooie, heldere weergave.
style.use('ggplot')

# Definieer een functie om een lijndiagram te maken.
def line():
    # Haal data op die nodig is voor het lijndiagram uit de database.
    data = Database.GetLineDiagramData()
    
    # Maak lijsten aan voor categorieën en totalen, op basis van de data.
    categories = [item["category"] for item in data]
    total = [item["total"] for item in data]

    # Roep de functie aan om het lijndiagram te maken met de categorieën en totalen.
    Line_diagram.Line_diagram.Createline(categories, total)

# Definieer een functie om een staafdiagram te maken.
def bar():
    # Haal data op die nodig is voor het staafdiagram uit de database.
    data = Database.GetBarDiagramData()

    # Maak lijsten aan voor categorieën, totalen en hoeveelheden uit de data.
    categories = [item["category"] for item in data]
    total = [item["total"] for item in data]
    quantity = [item["quantity"] for item in data]

    # Roep de functie aan om het staafdiagram te maken met deze lijsten.
    Bar_diagram.Bar_diagram.Createbar(categories, total, quantity)

# Definieer een functie om een cirkeldiagram te maken.
def circle():
    # Haal data op die nodig is voor het cirkeldiagram uit de database.
    data = Database.GetCircleDiagramData()

    # Maak lijsten aan voor categorieën en totalen, op basis van de data.
    categories = [item["category"] for item in data]
    total = [item["total"] for item in data]

    # Roep de functie aan om het cirkeldiagram te maken met de categorieën en totalen.
    Circel_diagram.Circel_diagram.CreateCirle(total, categories)

# Definieer een functie om een wireframe-diagram te maken.
def wireframe():
    # Haal data op die nodig is voor het wireframe-diagram uit de database.
    data = Database.GetWireframeDiagramData()

    # Maak lijsten aan voor datums, pizzanamen en hoeveelheden.
    date = [item["order_date"] for item in data]
    name = [item["pizza_name"] for item in data]
    quantity = [item["pizza_size"] for item in data]
    
    # Maak een 3D-wireframe door x- en y-coördinaten te maken en deze om te zetten naar een grid.
    for i in range(0, len(quantity)):
        x = np.linspace(date, name, quantity)
        y = np.linspace(date, name, quantity)
        x, y = np.meshgrid(x, y)
        
        # Gebruik een wiskundige functie om de z-coördinaten in te stellen.
        z = np.sin(np.sqrt(x**2 + y**2))

    # Roep de functie aan om het wireframe-diagram te maken met x, y en z.
    Wireframe_diagram.Wireframe_diagram.CreateWireFrame(x, y, z)

# Start de GUI (venster) door een Tk()-object te maken.
root = Tk()

# Maak een frame (een soort container) voor de GUI-knoppen en labels.
frm = ttk.Frame(root, padding=10)
frm.grid()

# Voeg een label toe aan de GUI die de gebruiker verwelkomt op het dashboard.
ttk.Label(frm, text="Welkom to my pizza dashboard").grid(column=0, row=0)

# Voeg een knop toe om het programma af te sluiten.
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=20, row=0)

# Voeg knoppen toe waarmee je de verschillende grafieken kunt openen.
ttk.Button(frm, text="line diagram", command=line).grid(column=0, row=5)
ttk.Button(frm, text="bar diagram", command=bar).grid(column=1, row=5)
ttk.Button(frm, text="circel", command=circle).grid(column=0, row=8)
ttk.Button(frm, text="wireframe", command=wireframe).grid(column=1, row=8)

# Start de GUI en wacht tot de gebruiker interactie heeft.
root.mainloop()



# import pandas as pd 
# from matplotlib import style
# from search_by_name import fileHandler
# from Diagram_components import Bar_diagram
# from Diagram_components import Circel_diagram
# from Diagram_components import Line_diagram
# from Diagram_components import Wireframe_diagram
# from sqlite_db import Database
# from tkinter import *
# from tkinter import ttk
# import numpy as np

# filename =  'Data_Model_Pizza_Sales.xlsx'
# #filePath = 'c:\\temp\\Data_Model_Pizza_Sales.xlsx'
# #df = pd.read_excel(filePath)
# style.use('ggplot')
# def line():
#     data =  Database.GetLineDiagramData()
    
#     categories = [item["category"] for item in data]
#     total = [item["total"] for item in data]

#     Line_diagram.Line_diagram.Createline(categories,total)

# #Bar graph
# def bar():
#     data =  Database.GetBarDiagramData()

    
#     categories = [item["category"] for item in data]
#     total = [item["total"] for item in data]
#     quantity = [item["quantity"] for item in data]

#     Bar_diagram.Bar_diagram.Createbar(categories,total,quantity)

# #Circle graph
# def circle():
#     data =  Database.GetCircleDiagramData()
#     categories = [item["category"] for item in data]
#     total = [item["total"] for item in data]

#     Circel_diagram.Circel_diagram.CreateCirle(total,categories)

# #wireframe
# def wireframe():
#     data =  Database.GetWireframeDiagramData()

#     date = [item["order_date"] for item in data]
#     name = [item["pizza_name"] for item in data]
#     quantity = [item["pizza_size"] for item in data]
#     for i in range(0 , len(quantity)):
#         x = np.linspace(date, name, quantity)
#         y = np.linspace(date, name, quantity)
#         x, y = np.meshgrid(x, y)
#         z = np.sin(np.sqrt(x**2 + y**2))

#     Wireframe_diagram.Wireframe_diagram.CreateWireFrame(x,y,z)    

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Welkom to my pizza dashboard").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=20, row=0)
# ttk.Button(frm, text="line diagram", command=line).grid(column=0, row=5)
# ttk.Button(frm, text="bar diagram", command=bar).grid(column=1, row=5)
# ttk.Button(frm, text="circel", command=circle).grid(column=0, row=8)
# ttk.Button(frm, text="wireframe", command=wireframe).grid(column=1, row=8)
# root.mainloop()

# #Line graph
