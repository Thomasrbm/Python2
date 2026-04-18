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

    year = '1900'

    # concat + dropna en une ligne, pas besoin de try/except
    # si '1900' manque pandas retourne colonne vide, dropna vide tout
    data = p.concat([df_income[year], df_life[year]],
                    axis=1, keys=['GDP', 'Life']).dropna()
    # concat un peut comme zip mais pour tableau, aligne par index
    # dropna supprime les lignes où il manque une valeur. faut val x et y

    # fait les points
    plt.scatter(data['GDP'], data['Life'])

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.xlim(300, 10000)

    plt.title("For the year 1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
