from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3

connection = sqlite3.connect('C:/temp/database.db')
cursor = connection.cursor()

class Bar_diagram: 
    def Createbar(df): 
        ax = sns.barplot(x='pizza_name', y='sum(quantity)', data= df, hue='pizza_category')
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation= 90)
        plt.title("staafDiagram")
        plt.xlabel("Categorieën")
        plt.ylabel("waarden")
        plt.show()