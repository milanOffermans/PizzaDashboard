from matplotlib import pyplot as plt
class Bar_diagram: 
    def Createbar(a, b): 
        plt.bar(a, b, color = "white")
        plt.title("staafDiagram")
        plt.xlabel("Categorieën")
        plt.ylabel("waarden")
        plt.show()