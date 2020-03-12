from math import pow, log
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid", {'xtick.top': False})
from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

x_range = np.arange(0,11)
y_exp = None
y_log = None

def exp_data(x):
    y = []
    for _ in x:
        tmp_ans = pow(2,_)
        y.append(tmp_ans)
    return y

def log_data(x):
    y = []
    for _ in x:
        if _ <= 0.0:
            y.append(float(_))
            continue
        tmp_ans = log(_,2)*300.0
        y.append(tmp_ans)
    return y

def SimpleLine(x,y):
        ax = plt.subplot(111)
        plt.plot(x,y, 'b--')
        #plt.bar(x,y, ecolor='black', capsize=4.0, align='center', edgecolor='black')
        y_label = "Y Data"
        plt.ylabel(y_label, fontsize=15)
        plt.yticks(fontsize=15)
        x_label = "X Range"
        plt.xlabel(x_label, fontsize=15)
        plt.xticks(x, [label for label in x], fontsize=15)
        # Personal preference (only horizontal lines across the plot)
        # comment-out to have squared (grid) pattern
        plt.grid(axis="x")
        # Show ticks on the left and bottom spines
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        # Remove ticks on the right and top spine (they shouldn't be required, uncommented if needed)
        # ax.spines['right'].set_visible(False)
        # ax.spines['top'].set_visible(False)
        plt.tight_layout()
        # For the highest quality plot I create .png files using 600 dpi
        # This kind of high quality plotting is required for thesis or journal papers, rather than conferences or reports
        # As low as 200 dpi is perfect for visualising, however for presentations and papers it shouldn't be lower than 300 dpi
        plt.savefig("SimpleLine.png", dpi=600)
        plt.show()
        plt.close()

def SimpleMultiLine(value_list):
    ax = plt.subplot(111)
    colours = ["blue", "red"]
    markers = ["o", "x"]
    for i, (x,y) in enumerate(value_list):
        plt.plot(x,y, color=colours[i], marker=markers[i])
    y_label = "Y Data"
    plt.ylabel(y_label, fontsize=15)
    plt.yticks(fontsize=15)
    x_label = "X Range"
    plt.xlabel(x_label, fontsize=15)
    plt.xticks(x, [label for label in x], fontsize=15)
    plt.grid(axis="x")
    # Show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.tight_layout()
    plt.savefig("SimpleMultiLine.png", dpi=600)
    plt.show()
    plt.close()
y_exp = exp_data(x_range)
y_log = log_data(x_range)

SimpleLine(x_range,y_log)
SimpleMultiLine([(x_range,y_exp),(x_range,y_log)])
