from matplotlib import pyplot as plt
class Line_diagram: 
    def Createline(x, y): 
        plt.plot(x,y)
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation= 90)
        plt.title("Lijngrafiek")
        plt.xlabel("Pizza_category")
        plt.ylabel("quantity")
        plt.show()