import pandas as p


def load(path: str) -> p.DataFrame:
    try:
        df = p.read_csv(path)
    except FileNotFoundError:
        print("Error: file not found.")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main():
    try:
        print(load("life_expectancy_years.csv"))
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
