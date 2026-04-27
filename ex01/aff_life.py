import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        return
    # iloc = idx par pos vs loc = par label y et x
    # [0, 1:]  0= premier lige 1:= sauf la premier colone toutes les cols
    country_data = df.query("country == 'France'").iloc[0, 1:]
    years = country_data.index.astype(int)
    values = country_data.values.astype(float)
    plt.figure("France Life expectancy")
    plt.plot(years, values)
    plt.xticks(range(1800, 2100, 40))
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
