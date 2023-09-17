import os
import matplotlib.pyplot as plt
from mylib.lib import read


def summary_statistics(csv):
    df = read(csv)
    summary = df.describe()
    summary.to_html("Output/decribe_summary.html", index=False)
    return summary


def scatterplot(csv):
    df = read(csv)
    x = df.iloc[:, 2]  # 3rd column (number of rooms)
    y = df.iloc[:, 4]  # 5th column (price)
    plt.scatter(x, y, alpha=0.5, label="Data Points")
    plt.title("Scatter Plot of Melbourne housing")
    plt.xlabel("Rooms")
    plt.ylabel("Price")
    plt.grid(True)
    plt.savefig("Output/Scatter_plot.png", format="png")
    plt.show()


def boxplot(csv):
    df = read(csv)
    df.boxplot(by="Type", column=["Price"], grid=False)
    plt.title("Boxplot: Melbourne Housing Price")
    plt.savefig("Output/boxplot.png", format="png")
    plt.show()


def piechart(csv):
    df = read(csv)
    df["Modified_Bedroom"] = df["Bedroom2"].apply(lambda x: "5+" if x >= 5 else str(x))
    bedroom_distribution = df["Modified_Bedroom"].value_counts()
    bedroom_distribution = bedroom_distribution.drop("nan", errors="ignore")
    plt.figure()
    plt.pie(bedroom_distribution, labels=bedroom_distribution.index, autopct="%1.1f%%")
    plt.title("Bedroom # distribution among all sellers")
    plt.axis("equal")
    plt.savefig("Output/Pie_chart.png", format="png")
    plt.show()


def output_directory(directory="Output"):
    """Create output directory"""
    os.makedirs(directory, exist_ok=True)
