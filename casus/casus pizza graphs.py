import pandas as pd 
from matplotlib import style
from search_by_name import fileHandler
from Diagram_components import Bar_diagram
from Diagram_components import Circel_diagram
from Diagram_components import Line_diagram

filename =  'Data_Model_Pizza_Sales.xlsx'
filePath = fileHandler.find_file(filename)
df = pd.read_excel(filePath)

#Line graph
style.use('ggplot')
x = [1, 2, 3]
y = [2, 4, 6]

Line_diagram.Line_diagram.Createline(x,y)

#Bar graph
a = ["Categorie 1", "Categorie 2", "Categorie 3"]
b = [22, 33, 44]

Bar_diagram.Bar_diagram.Createbar(a,b)

#Circle graph
labels = ["Categorie 1", "Categorie 2", "Categorie 3"]
sizes = [25, 35, 40]
explode = (0, 0.1, 0) 

Circel_diagram.Circel_diagram.CreateCirle(labels,sizes,explode)