import os
from script import summary_statistics, scatterplot, boxplot, piechart, output_directory


def test_output_directory():
    expected_directory = "Output"
    output_directory(expected_directory)
    assert os.path.exists(expected_directory)


def test_summary_statistics():
    file = "Melbourne_housing.csv"
    new = summary_statistics(file)
    assert new["Distance"].iloc[-1] == 48.100000
    assert new["Car"].iloc[0] == 26129.000000
    assert new["Landsize"].iloc[0] == 23047.000000


def test_scatterplot():
    scatterplot("Melbourne_housing.csv")


def test_boxplot():
    boxplot("Melbourne_housing.csv")


def test_piechart():
    piechart("Melbourne_housing.csv")


if __name__ == "__main__":
    test_summary_statistics()
    test_scatterplot()
    test_boxplot()
    test_piechart()
    test_output_directory()
