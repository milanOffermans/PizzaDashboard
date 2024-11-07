# Uitleg van wat de code doet:

# Deze code maakt een lijndiagram met gegevens over pizza-categorieën en de hoeveelheden daarvan.
# De x-as toont de pizza-categorieën, terwijl de y-as de hoeveelheden weergeeft.
# Door plt.xticks(rotation=90) zijn de labels op de x-as verticaal gedraaid, zodat lange namen beter passen.
# plt.show() toont de grafiek op het scherm.


# Importeer de pyplot-module uit de matplotlib-bibliotheek om grafieken te maken.
from matplotlib import pyplot as plt

# Maak een klasse genaamd Line_diagram. Deze klasse bevat functies om lijndiagrammen te maken.
class Line_diagram:
    
    # Definieer een functie genaamd Createline die een lijndiagram maakt.
    # De functie neemt twee parameters mee:
    # - x: de gegevens voor de x-as (bijvoorbeeld de categorieën van pizza's)
    # - y: de gegevens voor de y-as (bijvoorbeeld de hoeveelheden)
    def Createline(x, y):
        
        # Teken het lijndiagram met de gegevens in 'x' (x-as) en 'y' (y-as).
        plt.plot(x, y)
        
        # Pas de marges onderaan het diagram aan, zodat er meer ruimte is voor de labels.
        plt.subplots_adjust(bottom=0.25)
        
        # Draai de labels op de x-as (de namen) 90 graden om ze beter leesbaar te maken.
        plt.xticks(rotation=90)
        
        # Voeg een titel toe aan het lijndiagram.
        plt.title("Lijngrafiek")
        
        # Geef de x-as de naam "Pizza_category" om aan te geven wat erop staat.
        plt.xlabel("Pizza_category")
        
        # Geef de y-as de naam "quantity" om aan te geven wat deze gegevens betekenen.
        plt.ylabel("quantity")
        
        # Toon het lijndiagram op het scherm.
        plt.show()



# from matplotlib import pyplot as plt
# class Line_diagram: 
#     def Createline(x, y): 
#         plt.plot(x,y)
#         plt.subplots_adjust(bottom=0.25)
#         plt.xticks(rotation= 90)
#         plt.title("Lijngrafiek")
#         plt.xlabel("Pizza_category")
#         plt.ylabel("quantity")
#         plt.show()