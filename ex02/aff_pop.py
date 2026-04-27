import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("population_total.csv")
    if df is None:
        return

    df = df.set_index(df.columns[0])
    # change les lettres pas notation scientifiaue usable
    for col in df.columns:
        df[col] = (df[col].astype(str)
                          .str.replace('M', 'e6')
                          .str.replace('k', 'e3')
                          .str.replace('B', 'e9')
                          .astype(float))
    country_1, country_2 = "Belgium", "France"

    # filtre et prend que si l'année est dans le csv
    years = [str(y) for y in range(1800, 2051) if str(y) in df.columns]
    x_years = [int(y) for y in years]

    # plot fait la courbe
    # df.loc["France"] toute la ligne France (tous les années)
    # df.loc["France", "1800"]  valeur unique : population France en 1800
    # df.loc["France", ["1800", "1801", "1802"]]

    # plt.plot([1800], [28000000])  # un seul point → invisible
    plt.plot(x_years, df.loc[country_1, years], label=country_1)
    plt.plot(x_years, df.loc[country_2, years], label=country_2, color='green')

    # lambda reçoit x=valeur brute, _=position (ignorée)
    # transforme 20000000 → "20M"
    formatter = plt.FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
    # gca() = "get current axes" = récupère le graphique actif
    # .yaxis = l'axe Y
    # .set_major_formatter() = applique le formateur aux graduations
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.yticks([20_000_000, 40_000_000, 60_000_000])
    plt.xticks(range(1800, 2051, 40))
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.tight_layout()
    # ajuste automatiquement les marges pour que
    # rien ne soit coupé (titre, labels, légende)
    plt.show()


if __name__ == "__main__":
    main()
