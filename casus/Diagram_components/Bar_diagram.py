# Uitleg van wat de code doet:

# Deze code maakt een staafdiagram met gegevens over categorieën en hun bijbehorende waarden.
# De x-as toont de verschillende categorieën, en de y-as geeft de waarden aan die bij elke categorie horen.
# Door de draaiing van de labels op de x-as kunnen lange namen goed worden weergegeven. 
# Na het instellen van alle eigenschappen, toont plt.show() het diagram aan de gebruiker.


# Importeer de pyplot-module uit de matplotlib-bibliotheek om grafieken te maken.
from matplotlib import pyplot as plt

# Maak een klasse genaamd Bar_diagram. Deze klasse zal functies bevatten om staafdiagrammen te maken.
class Bar_diagram:
    
    # Definieer een functie genaamd Createbar die een staafdiagram maakt.
    # De functie neemt drie parameters mee:
    # - a: de categorieën die op de x-as (horizontale as) komen
    # - b: de waarden die bij elke categorie horen en op de y-as (verticale as) komen
    # - c: wordt hier niet gebruikt, maar kan bijvoorbeeld een andere dataset zijn die we in de toekomst willen toevoegen
    def Createbar(a, b, c):
        
        # Maak een staafdiagram met de categorieën in 'a' en de waarden in 'b'.
        # Stel de kleur van de staven in op wit.
        plt.bar(a, b, color="white")
        
        # Pas de marges onderaan het diagram aan, zodat er meer ruimte is voor de labels.
        plt.subplots_adjust(bottom=0.25)
        
        # Draai de labels op de x-as (categorieën) 90 graden zodat ze verticaal staan, voor betere leesbaarheid.
        plt.xticks(rotation=90)
        
        # Geef het diagram een titel.
        plt.title("Staafdiagram")
        
        # Voeg een label toe aan de x-as, dat aangeeft dat hier categorieën staan.
        plt.xlabel("Categorieën")
        
        # Voeg een label toe aan de y-as, dat aangeeft dat hier waarden staan.
        plt.ylabel("Waarden")
        
        # Toon het staafdiagram op het scherm.
        plt.show()



# from matplotlib import pyplot as plt
# class Bar_diagram: 
#     def Createbar(a, b, c): 
#         plt.bar(a, b, color = "white")
#         plt.subplots_adjust(bottom=0.25)
#         plt.xticks(rotation= 90)
#         plt.title("staafDiagram")
#         plt.xlabel("Categorieën")
#         plt.ylabel("waarden")
#         plt.show()