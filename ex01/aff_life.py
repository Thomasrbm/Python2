import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        return
    country_data = df[df["country"] == "France"].iloc[0, 1:]
    # iloc 0,1  ligne colone.  premier ligne 0, toutes les col sauf la 1ere
    # start a 1
    years = country_data.index.astype(int)
    values = country_data.values.astype(float)
    # index et value des cols
    plt.figure("France Life expectancy")
    plt.plot(years, values)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
