from matplotlib import pyplot as plt
class Bar_diagram: 
    def Createbar(a, b, c): 
        plt.bar(a, b, color = "white")
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation= 90)
        plt.title("staafDiagram")
        plt.xlabel("Categorieën")
        plt.ylabel("waarden")
        plt.show()