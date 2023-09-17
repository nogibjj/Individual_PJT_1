from mylib.lib import read
import pandas as pd


def test_read():
    file = "Melbourne_housing.csv"
    df = read(file)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


if __name__ == "__main__":
    test_read()
