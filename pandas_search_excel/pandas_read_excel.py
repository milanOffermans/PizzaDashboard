import pandas as pd


#file path krijg je met de andere functie
df = pd.read_excel(file_path)
data_dict= = df.set_index("key")["Value"].to_dict()