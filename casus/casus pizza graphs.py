import pandas as pd 
from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import style

#leest CSV file.
path = Path.cwd()
d = pd.read_csv(str(path) + "GlobalLandTemperaturesByCountry.csv")
d.columns

#Line graph
style.use()
x = [1,1,1]
y= [2,2,2]
x2= [3,3,3]
y2 = [4,4,4]

plt.plot(x,y)
fig = plt.figure()
plt.title("")
plt.xlabel("X as")
plt.ylabel("y as")
plt.show

#Bar graph
a = ["","",""]
b = [22, 33, 44]
plt.bar(a, b, color = "white")
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()

#Circle graph
a = ""
b = []
explode = ()
fig1, a1 = plt.subplots()
a1.pie(b, explode = explode, labels = a, autopct = "%2.2%%", shadow = True, startangle = 100)
a1.ais("equal") #Zorgt voor een cirkel.
plt.show()