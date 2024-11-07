# Uitleg van wat de code doet:

# Deze code maakt een 3D-wireframe-diagram. De x-, y- en z-coördinaten bepalen de punten in de 3D-ruimte waarop lijnen getrokken worden.
# Het wireframe wordt getekend in een speciale 3D-subplot, die door projection='3d' wordt gemaakt.
# De grafiek wordt weergegeven in een figuur, zodat je een driedimensionaal beeld ziet van de gegevens.
# plt.show() laat de grafiek op het scherm zien.


# Importeer de pyplot-module uit de matplotlib-bibliotheek voor het maken van 3D-grafieken.
import matplotlib.pyplot as plt

# Maak een klasse genaamd Wireframe_diagram. Deze klasse bevat functies om 3D-wireframe-diagrammen te maken.
class Wireframe_diagram:
    
    # Definieer een functie genaamd CreateWireFrame die een 3D-wireframe-diagram maakt.
    # De functie neemt drie parameters:
    # - x: een reeks x-coördinaten voor de grafiek (horizontale as)
    # - y: een reeks y-coördinaten voor de grafiek (diepte-as)
    # - z: een reeks z-coördinaten voor de grafiek (verticale as)
    def CreateWireFrame(x, y, z):
        
        # Maak een nieuwe figuur aan, waarin het wireframe wordt getekend.
        fig = plt.figure()
        
        # Voeg een 3D-subplot toe aan de figuur. Dit betekent dat we een 3D-ruimte hebben om de grafiek in te tekenen.
        # '1,2,2' verdeelt de figuur in een grid en kiest positie 2 voor de grafiek.
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        
        # Teken het wireframe in de 3D-ruimte met de x-, y-, en z-coördinaten.
        ax.plot_wireframe(x, y, z)
        
        # Toon de figuur met het wireframe aan de gebruiker.
        plt.show()



# import matplotlib.pyplot as plt
# class Wireframe_diagram:
#     def CreateWireFrame(x,y,z):
#         fig = plt.figure()
#         ax = fig.add_subplot(1,2,2, projection='3d')
#         ax.plot_wireframe(x, y, z)
#         plt.show()