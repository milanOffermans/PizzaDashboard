# Uitleg van wat de code doet:

# Deze code zoekt naar een bestand in een opgegeven map en al zijn submappen. Als je bijvoorbeeld een bestand met de naam 
# "document.txt" zoekt, hoef je alleen de naam op te geven en een map 
# (als je geen specifieke map invult, zoekt de code in de huidige map waar de code draait). 
# Zodra het bestand wordt gevonden, geeft de code het volledige pad terug waar het bestand zich bevindt. 
# Als het bestand niet wordt gevonden, geeft de code aan dat het er niet is.

# Importeer de Path-functie uit de pathlib-bibliotheek, zodat we gemakkelijk met bestanden en mappen kunnen werken.
from pathlib import Path

# Maak een nieuwe klasse (soort blauwdruk) genaamd fileHandler. Hiermee gaan we straks bestanden zoeken.
class fileHandler:
    
    # Maak een functie die een bestand kan vinden. De functie heet 'find_file' en neemt twee dingen mee:
    # 1. de naam van het bestand dat je zoekt (filename)
    # 2. de plek waar je wilt zoeken (search_path). Als je geen plek opgeeft, zoekt hij in de huidige map.
    def find_file(filename, search_path=''):
        
        # Zet de zoekmap om in een Path-object, zodat we er gemakkelijker mee kunnen werken in de code.
        search_dir = Path(search_path)
        
        # Loop door alle bestanden in de map en submappen die overeenkomen met de naam van het bestand dat je zoekt.
        for file_path in search_dir.rglob(filename):
            # Zodra je het bestand vindt, geef je het pad (locatie) van het bestand terug en stop je de functie.
            return file_path
        
        # Als de functie klaar is met zoeken en geen bestand heeft gevonden, geef dan 'None' terug (dat betekent "niks gevonden").
        return None



# from pathlib import Path
# class fileHandler:
#     def find_file(filename, search_path=''):
#         search_dir = Path(search_path)
#         for file_path in search_dir.rglob(filename):
#             return file_path
#         return None