# Written in python 3.6.9 (should work for all python versions >= 3.6)
# Libraries (will all be explained soon...)
import csv
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid", {'xtick.top': False})
from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

'''
==================================================
All code and working will be explained soon...
==================================================
'''


# Nothing special, a very clean and basic barplot function (contains no title)
def SimpleBar(x,y,y_error):
    ax = plt.subplot(111)
    plt.bar(x,y, yerr=y_error, ecolor='black', capsize=4.0, align='center', edgecolor='black')
    #plt.bar(x,y, ecolor='black', capsize=4.0, align='center', edgecolor='black')
    y_label = "Average Heights"
    plt.ylabel(y_label, fontsize=15)
    plt.yticks(fontsize=15)
    x_label = "Age"
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
    plt.savefig("SimpleBar.png", dpi=600)
    plt.show()
    plt.close()


# Sticking with the clean and basic (multi) barplot function (no title)
def SimpleMultiBar(datasets=[]):
    if len(datasets) == 2:
        # the x_axis should remind the same for all the datasets (this needs to be known/expected)
        # here I have redefined it to 'int' values so it can be used for the x_axis in the bar plots
        x_range = [10, 20, 30]
        y_list = []
        yerr_list = []
        y_max = 0
        for y,yerr in datasets:
            y_list.append(y)
            yerr_list.append(yerr)
            if y_max < max(y): y_max = max(y)
        ax = plt.subplot(111)
        # the width of the bars
        width = 3.0
        ax.bar([x- width/2 for x in x_range], y_list[0], yerr=yerr_list[0], width=width, ecolor='black', capsize=4.0, color='#0496ff', align='center', edgecolor='black', label="Male")
        ax.bar([x+ width/2 for x in x_range], y_list[1], yerr=yerr_list[1], width=width, ecolor='black', capsize=4.0, color='#006ba6', align='center', edgecolor='black', label="Female")
        plt.yticks(fontsize=15)
        y_label = "Average Height"
        plt.ylabel(y_label, fontsize=15)
        plt.yticks(fontsize=15)
        x_label = "Age"
        plt.xlabel(x_label, fontsize=15)
        plt.xticks(x_range, [label for label in ageList], fontsize=15)
        plt.grid(axis="x")
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        plt.ylim(0, y_max+(y_max*0.5))
        ax.legend(fontsize=15)
        plt.tight_layout()
        plt.savefig("SimpleMultiBar.png", dpi=600)
        plt.show()
        plt.close()
    else:
        print ("This is a simple function for 2 datasets. \nChange \"SimpleMultiBar\" function for custom number of datasets.")


def SimpleStackedBar(datasets=[]):
    if len(datasets) == 2:
        # expand your own colour scheme if the datasets are more than 2 
        # (e.g. a great colour scheme I like can be found on "https://coolors.co/006ba6-0496ff-403f4c-2dc7ff-e84855")
        colours = ['#0496ff','#006ba6']
        # the x_axis should remind the same for all the datasets (this needs to be known/expected)
        # here I have redefined it to 'int' values so it can be used for the x_axis in the bar plots
        x_range = [10, 20, 30]  
        y_list = []
        yerr_list = []
        y_max = 0
        for y,yerr in datasets:
            y_list.append(y)
            yerr_list.append(yerr)
            if y_max < max(y): y_max = max(y)
        # initial bottoms is zero in the datasets array
        bottoms = plt.bar(x_range, y_list[0],yerr=yerr_list[0], capsize=4, color=colours[0], linewidth=1.25, edgecolor='black', width=3.0, align='center', ecolor='black') 
        # for loop allows as many bars as you wish to stack on top of the initial (bottom) bar
        for i in range(1, len(datasets)):
            bar_color = colours[i]
            plt.bar(x_range, y_list[i], yerr=yerr_list[i], capsize=4, color=bar_color, linewidth=1.25, edgecolor='black', width=3.0, align='center', bottom=y_list[0], ecolor='black')
        ax = plt.subplot(111)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        legend_labels = ["Male", "Female"]
        plt.legend(legend_labels, loc='upper left', ncol=1, fancybox=True, shadow=False)
        plt.yticks(fontsize=15)
        y_label = "Average Heights (Stacked)"
        plt.ylabel(y_label, fontsize=15)
        plt.grid(axis="x")
        x_label = "Age"
        plt.xlabel(x_label, fontsize=15)
        plt.xticks(x_range, [label for label in x_range], fontsize=15)
        plt.ylim(0, y_max+(y_max*1.5))
        plt.tight_layout()
        plt.savefig("SimpleStackedBar.png", dpi=600)
        plt.show()
        plt.close()
    else:
        print ("This is a simple function for 2 datasets. \nChange \"SimpleStackedBar\" function for custom number of datasets.")


# Random variables to generate fake data (i.e. age and height)
sample_size = 100
genders = 2 # 1 - "could" indicate a mixed (male and female) dataset, 2 - indicates a separated dataset for male and female
# np.random.seed(42)  # uncomment this to obtain the same standard deviation seen in the demo plots
# Create random age list
ageList = ['10', '20', '30'] 

def dataConstructor(age, random_std):
    if age == "10": y_out = [np.random.normal(150, 25*random_std) for sample in range(sample_size)]
    elif age == "20": y_out = [np.random.normal(175, 20*random_std) for sample in range(sample_size)]
    else: y_out = [np.random.normal(175, 15*random_std) for sample in range(sample_size)]
    y_mean = np.mean(y_out)
    y_error = (np.std(y_out))
    return (y_mean, y_error)

def dataGenerator(sample_size, genders, datalist):
    lists_of_ymean = []
    lists_of_yerr = []
    list_of_datasets = []
    if genders == 1:
        for age in datalist:
            ymean, yerr = dataConstructor(age, np.random.uniform(0.0, 0.5))
            lists_of_ymean.append(ymean)
            lists_of_yerr.append(yerr)
        list_of_datasets.append((lists_of_ymean, lists_of_yerr))
        return list_of_datasets
    elif isinstance(genders, int) and genders >1:
        for gender in range(genders):
            lists_of_ymean = []
            lists_of_yerr = []
            for age in datalist:
                ymean, yerr = dataConstructor(age, np.random.uniform(0.0, 0.5))
                lists_of_ymean.append(ymean)
                lists_of_yerr.append(yerr)
            list_of_datasets.append((lists_of_ymean, lists_of_yerr))
        return list_of_datasets

# generate my random data (note: does not have to be age and height data, this is just my silly example)
random_datasets = dataGenerator(sample_size, genders, ageList)
# pass only a single dataset to the simplebar function and plot...
lists_yout, lists_yerr = random_datasets[0]
SimpleBar(ageList, lists_yout, lists_yerr)
# pass the random dataset to the multibar function and plot...
SimpleMultiBar(datasets=random_datasets)
# same as above and plot...
SimpleStackedBar(datasets=random_datasets)