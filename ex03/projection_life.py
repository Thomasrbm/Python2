from load_csv import load
import matplotlib.pyplot as plt
import pandas as p


def main():
    df_income = load("income.csv")
    df_life = load("life_expectancy_years.csv")
    if df_income is None or df_life is None:
        return

    df_income = df_income.set_index(df_income.columns[0])
    df_life = df_life.set_index(df_life.columns[0])

    # prend des 2 csv les val pour 1900 dans un df, idx + dico
    data = p.concat([df_income['1900'], df_life['1900']],
                    axis=1, keys=['GDP', 'Life']).dropna()
    # concat un peut comme zip mais pour tableau, aligne par index
    # dropna supprime les lignes où il manque une valeur. faut val x et y

    # fait les points
    plt.scatter(data['GDP'], data['Life'])

    # pas espacement constant mais puissance de 10
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
