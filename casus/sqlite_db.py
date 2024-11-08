import sqlite3
import pandas as pd
from search_by_name import fileHandler
class Database:
    
    def Create_Database(filename):
        filePath = "C:/Users/juria_rfq14t7/Documents/Data Model - Pizza Sales.xlsx"
        PizzaList = []
        df = pd.read_excel(filePath)
        df.columns = df.columns.str.strip()

        # Haalt extra white spaces enz weg waardoor je een cleaner resultaat krijgt bij een query.    
        connection = sqlite3.connect("C:/Users/juria_rfq14t7/Documents/database.db")
        cursor = connection.cursor()
        
        #Hier maar ik eerst een connectie met de database. Indien er geen bestaat word eentje gemaakt met de opgegeven naam in mijn geval database.db.
        #de cursor opbject moet je zien als een daadwerkelijk cursor (muis). deze kun je naar een table sturen en zeggen dat die iets uit die table moet selecteren en die kun je vervolgens zien.

        try:
            df.to_sql('Pizza_Database', connection, if_exists='replace')
        
            #Hier met de pandas libary zorg ik ervoor dat de df(dataframe) die met pandas gemaakt is over word gezet naar de database.
            #De eerste argument is de naam van de table 2de argument is de database die we geconnect hebben / gemaakt hebben. het laatse argument kun je aangeven wat je wilt doen in t geval van dupes.
        

            connection.commit()
        
            #Dit is net als bij github alle changes gaan pas officieel door zodra je het commit vandaar dus de commit functie gecalled op het connection object oftwel de database.
        
            cursor.execute('''
            SELECT distinct(pizza_category), sum(quantity) as quant from 'Pizza_Database'
            group by pizza_category order  by quant desc 
            ''')
        
            for row in cursor.fetchall():
                PizzaList.append(row[0], row[1])
                print(f'Category: {row[0]}, Total sum: {row[1]}')

            return PizzaList
            #cursor.execute('SELECT * FROM Pizza_Database')
            #print(cursor.fetchone())
        
            #Om de cursor iets te laten doen heb je de execute functie met de argument een string waarin je vertelt wat je wilt. in dit geval zeg ik selecteer van de Pizza_Database table.
            #Zodra ik deze functie call gebeurt er nog niks de cursor(muis) heeft de table alleen geselecteerd met de print functie fetchone() zeg ik tegen de muis dat ik de info van de eerste rij wil.
            #Gerbuik je de fetchall pakt die alles en met de fetchmany kun je een range aangeven.
            #wil je alle data gebruiken kun je beter de code hieronder pakken voor een mooier resultaat.
        
            #for row in cursor.execute('SELECT * FROM Pizza_Database')
            #print(row)
        
            #De code hierboven haalt alle rows uit die table en print ze netjes onder elkaar om het gemakkelijk te kunne lezen.
            
            #id = ('ital_supr_l',)
            #cursor.execute('SELECT * FROM Pizza_Database WHERE pizza_id = ?', id)
            #print(cursor.fetchone())
        
            #Hier wil ik een specifieke row hebben voor de pizza_id ital_supr_l. dus maak ik een variable aan tussen haakjes met de naam en na de string een comma!!! anders werkt het niet.
            #Dan met de execute zeg ik weer select van from een table daarna zeg ik where dan de naam van de colom = ? en dan komma met de voorheen gemaakte variable.
            #Dan print ik weer de cursor.fetchone() en omdat ik de cursor(muis) naar die regel heb gebracht print die dus niet meer de eeste regel maar de regel die ik wil.
            #Heb ik niet specifiek gezegd waar de cursor heen moet in die table print die dus de eerste row. 
        except:
            print(f"connection failed: {connection.Error}")
        finally:
            connection.close()
        #Het is niet nodig maar wel goed om altijd de database weer te sluiten zodra je klaar bent met je acties dus leer je dit gewoon aan.

    def GetLineDiagramData():
        connection = sqlite3.connect('C:/Users/juria_rfq14t7/Documents/database.db')
        cursor = connection.cursor()
        Pizzalist = []

        try:
        
            cursor.execute('''
            SELECT distinct (pizza_id), sum(quantity) as quant from Pizza_Database group by pizza_id order  by quant desc LIMIT 0,10
            ''')
        
            for row in cursor.fetchall():
                pizzadict = {   'category': row[0],
                                'total': row[1]}
                Pizzalist.append(pizzadict)

            return Pizzalist
        except Exception as e:
             print(f"error : {str(e)}") 
        finally:
            connection.close()
    def GetCircleDiagramData():
        connection = sqlite3.connect('C:/Users/juria_rfq14t7/Documents/database.db')
        cursor = connection.cursor()
        Pizzalist = []

        try:
        
            cursor.execute('''
            SELECT distinct(pizza_category), sum(quantity) as quant from 'Pizza_Database'
            group by pizza_category order  by quant desc
            ''')
        
            for row in cursor.fetchall():
                pizzadict = {   'category': row[0],
                                'total': row[1]}
                Pizzalist.append(pizzadict)

            return Pizzalist
        except Exception as e:
             print(f"error : {str(e)}") 
        finally:
            connection.close()
    def GetBarDiagramData():
        connection = sqlite3.connect('C:/Users/juria_rfq14t7/Documents/database.db')
        cursor = connection.cursor()
        Pizzalist = []
        
        try:
        
            cursor.execute('''
            Select pizza_category, pizza_name, sum(quantity) from Pizza_Database group by pizza_category, pizza_name
            ''')
        
            for row in cursor.fetchall():
                pizzadict = {
                                'total': row[1],
                                'sum': row[2]}
                Pizzalist.append(pizzadict)

            return Pizzalist
        except Exception as e:
             print(f"error : {str(e)}") 
        finally:
            connection.close()
    def GetWireframeDiagramData():
        connection = sqlite3.connect('C:/Users/juria_rfq14t7/Documents/database.db')
        cursor = connection.cursor()
        Pizzalist = []

        try:
        
            cursor.execute('''
            Select order_date, pizza_name, pizza_size, sum(quantity) from Pizza_Database group by order_date, pizza_name, pizza_size
            ''')
        
            for row in cursor.fetchall():
                pizzadict = {   'order_date': row[0],
                                'pizza_name': row[1],
                                'pizza_size': row[3]}
                Pizzalist.append(pizzadict)

            return Pizzalist
        except Exception as e:
             print(f"error : {str(e)}") 
        finally:
            connection.close()

