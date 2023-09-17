import os
import matplotlib.pyplot as plt
from lib import read 
import pandas as pd


def summary_statistics(csv):
    df = read(csv)
    summary = df.describe()
    summary.to_html("output/decribe_summary.html", index=False) 
    return summary 

def scatterplot(csv):
    df = read(csv)
    x = df.iloc[:, 2] # 3rd column (number of rooms)
    y = df.iloc[:, 4] # 5th column (price)
    plt.scatter(x, y, alpha=0.5, label="Data Points")
    plt.title('Scatter Plot of Melbourne housing')
    plt.xlabel('Rooms')
    plt.ylabel('Price')
    plt.grid(True)
    plt.savefig("output/scatter.png", format="png")
    plt.show()

def boxplot(csv):
    df = read(csv)
    df.boxplot(by = 'Type', column=['Price'], grid = False)
    plt.savefig(output_path, format="png")
    plt.title("Boxplot: Melbourne Hosuing Price")
    plt.savefig("output/boxplot.png", format="png")
    plt.show()

def piechart(csv):
    df = read(csv)
    bedroom = df.iloc[:, 10] # 11th column (Bedroom2)
    seller = df.iloc[:, 6] # 7th column (SellerG)
    plt.pie(bedroom, seller, autopct="%.1f")
    plt.axes().set_aspect("equal")
    plt.title("Bedroom # distribution by seller")
    plt.savefig("output/boxplot.png", format="png")
    plt.show()

def output_directory(directory="Output"):
    """Create output directory"""
    os.makedirs(directory, exist_ok=True)