from matplotlib import pyplot as plt
class Circel_diagram: 
    def CreateCirle(data, category): 
        fig1, a1 = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation= 90)
        a1.pie(data,labels= category, autopct="%1.1f%%" ,startangle=90)
        a1.axis("equal") #Zorgt voor een cirkel.
        plt.title("Cirkelgrafiek")
        plt.show()