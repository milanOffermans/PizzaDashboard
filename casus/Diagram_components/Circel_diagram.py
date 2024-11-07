# Uitleg van wat de code doet:

# Deze code maakt een cirkeldiagram met data die je invoert. De segmenten in de cirkel worden gelabeld
# met de categorieën en tonen automatisch het percentage van elk segment. 
# Door a1.axis("equal") wordt de vorm gecorrigeerd naar een perfecte cirkel. plt.show() toont de grafiek aan de gebruiker.


# Importeer de pyplot-module uit de matplotlib-bibliotheek om grafieken te maken.
from matplotlib import pyplot as plt

# Maak een klasse genaamd Circel_diagram. Deze klasse zal functies bevatten om cirkeldiagrammen te maken.
class Circel_diagram:
    
    # Definieer een functie genaamd CreateCirle die een cirkeldiagram maakt.
    # De functie neemt twee parameters:
    # - data: een lijst met waarden die in het cirkeldiagram worden getoond.
    # - category: een lijst met labels voor elke waarde in de data, die de segmenten benoemen.
    def CreateCirle(data, category):
        
        # Maak een figuur en een enkele as (a1) om het cirkeldiagram te tekenen.
        fig1, a1 = plt.subplots()
        
        # Pas de marges onderaan het diagram aan voor meer ruimte.
        plt.subplots_adjust(bottom=0.25)
        
        # Draai de labels op de x-as 90 graden (hoewel dit in dit geval niet echt nodig is voor een cirkeldiagram).
        plt.xticks(rotation=90)
        
        # Teken het cirkeldiagram met de data en categorieën:
        # - 'labels=category' geeft de namen aan elk segment.
        # - 'autopct="%1.1f%%"' toont de percentages in elk segment.
        # - 'startangle=90' draait de grafiek zodat deze vanaf de bovenkant begint.
        a1.pie(data, labels=category, autopct="%1.1f%%", startangle=90)
        
        # Zorg ervoor dat de cirkel een echte cirkelvorm heeft en niet ovaal wordt weergegeven.
        a1.axis("equal")
        
        # Geef het diagram een titel.
        plt.title("Cirkelgrafiek")
        
        # Toon het cirkeldiagram op het scherm.
        plt.show()



# from matplotlib import pyplot as plt
# class Circel_diagram: 
#     def CreateCirle(data, category): 
#         fig1, a1 = plt.subplots()
#         plt.subplots_adjust(bottom=0.25)
#         plt.xticks(rotation= 90)
#         a1.pie(data,labels= category, autopct="%1.1f%%" ,startangle=90)
#         a1.axis("equal") #Zorgt voor een cirkel.
#         plt.title("Cirkelgrafiek")
#         plt.show()