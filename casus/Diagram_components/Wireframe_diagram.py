import matplotlib.pyplot as plt
class Wireframe_diagram:
    def CreateWireFrame(x,y,z):
        fig = plt.figure()
        ax = fig.add_subplot(1,2,2, projection='3d')
        ax.plot_wireframe(x, y, z)
        plt.show()