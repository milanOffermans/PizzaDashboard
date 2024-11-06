from matplotlib import pyplot as plt
class Circel_diagram: 
    def CreateCirle(labels, sizes, explode): 
        fig1, a1 = plt.subplots()
        a1.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
        a1.axis("equal") #Zorgt voor een cirkel.
        plt.title("Cirkelgrafiek")
        plt.show()