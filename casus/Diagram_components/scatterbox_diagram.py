import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime


class scatterbox_diagram:
    def Createscatterbox(x,y,z):
        dates = [datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') for date_str in x]
        numeric_dates = np.array([mdates.date2num(date) for date in dates])

        unique_strings = list(set(y))
        string_to_num = {string: idx for idx, string in enumerate(unique_strings)}
        numeric_strings = np.array([string_to_num[s] for s in y])

        numeric_ints = np.array(z)

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')
        
        ax.scatter(numeric_dates, numeric_strings, numeric_ints)
        plt.title("scatterbox")
        plt.xticks(rotation= 90)
        plt.yticks(rotation= 90)


        ax.set_yticks(list(string_to_num.values()))
        ax.set_yticklabels(unique_strings)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.show()