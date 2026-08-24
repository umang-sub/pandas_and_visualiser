import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys


class SalesDataFrame:
    def __init__(self):
        self.data = None

    def load(self, filepath):
        self.data = pd.read_csv(filepath)
        print("Dataset loaded successfully!")

    def __del__(self):
        self.data = None

    def explore(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Explore Data ---")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display basic info")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print(self.data.head())
        elif choice == "2":
            print(self.data.tail())
        elif choice == "3":
            print(self.data.columns.tolist())
        elif choice == "4":
            print(self.data.info())
            print(self.data.dtypes)
        else:
            print("Invalid choice.")

    def reset(self, other=None):
        if other is not None:
            self.data = other.data.copy() if other.data is not None else None
        else:
            self.data = None

    def mathematical(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            print("No numeric columns found.")
            return
        print(f"\nNumeric columns: {numeric_cols}")
        col = input("Enter column name for mathematical operations: ").strip()
        if col not in numeric_cols:
            print("Invalid column.")
            return
        print(f"Sum: {self.data[col].sum()}")
        print(f"Mean: {self.data[col].mean()}")
        print(f"Median: {self.data[col].median()}")
        print(f"Std: {self.data[col].std()}")
        print(f"Min: {self.data[col].min()}")
        print(f"Max: {self.data[col].max()}")

    def combine(self, other, how="inner", on=None):
        if self.data is None or other.data is None:
            print("One or both datasets not loaded.")
            return None
        if on:
            return pd.merge(self.data, other.data, how=how, on=on)
        return pd.concat([self.data, other.data], ignore_index=True)

    def create_pivot(self, index, columns, values, aggfunc="sum"):
        if self.data is None:
            return None
        return pd.pivot_table(self.data, index=index, columns=columns, values=values, aggfunc=aggfunc)

    def split(self, col=None, value=None, regex=None):
        if self.data is None:
            return None, None
        if col and value is not None:
            mask = self.data[col] == value
            return self.data[mask].reset_index(drop=True), self.data[~mask].reset_index(drop=True)
        if col and regex:
            mask = self.data[col].astype(str).str.contains(regex, na=False)
            return self.data[mask].reset_index(drop=True), self.data[~mask].reset_index(drop=True)
        mid = len(self.data) // 2
        return self.data.iloc[:mid].reset_index(drop=True), self.data.iloc[mid:].reset_index(drop=True)

    def search_sort(self, col=None, value=None, ascending=True, top_n=None):
        if self.data is None:
            return None
        result = self.data.copy()
        if col and value is not None:
            result = result[result[col] == value]
        if col:
            result = result.sort_values(by=col, ascending=ascending)
        if top_n:
            result = result.head(top_n)
        return result

    def filter(self, col, condition, value):
        if self.data is None:
            return None
        ops = {
            ">": self.data[col] > value,
            "<": self.data[col] < value,
            "==": self.data[col] == value,
            ">=": self.data[col] >= value,
            "<=": self.data[col] <= value,
            "!=": self.data[col] != value,
        }
        return self.data[ops[condition]] if condition in ops else None

    def aggregate(self, col, func="sum"):
        if self.data is None:
            return None
        funcs = {
            "sum": self.data[col].sum,
            "mean": self.data[col].mean,
            "min": self.data[col].min,
            "max": self.data[col].max,
            "count": self.data[col].count,
            "median": self.data[col].median,
        }
        return funcs[func]() if func in funcs else None

    def statistical(self):
        if self.data is None:
            return None
        return self.data.describe()

    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Data Visualization ---")
        print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram\n6. Heatmap\n7. Stack Plot")
        choice = input("Enter your choice: ").strip()
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()

        if choice == "1":
            x_col = input("Enter x-axis column name: ").strip()
            y_col = input("Enter y-axis column name: ").strip()
            plt.figure(figsize=(10, 6))
            self.data.groupby(x_col)[y_col].sum().plot(kind="bar", color="steelblue")
            plt.title(f"{y_col} by {x_col}")
            plt.tight_layout()
            plt.show()

        elif choice == "2":
            x_col = input("Enter x-axis column name: ").strip()
            y_col = input("Enter y-axis column name: ").strip()
            plt.figure(figsize=(10, 6))
            plt.plot(self.data[x_col], self.data[y_col], marker="o")
            plt.title(f"{y_col} over {x_col}")
            plt.tight_layout()
            plt.show()

        elif choice == "3":
            x_col = input("Enter x-axis column name: ").strip()
            y_col = input("Enter y-axis column name: ").strip()
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data[x_col], self.data[y_col], alpha=0.7, color="coral")
            plt.title(f"Scatter: {x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.tight_layout()
            plt.show()

        elif choice == "4":
            col = input("Enter column name for Pie Chart: ").strip()
            plt.figure(figsize=(8, 8))
            self.data[col].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140)
            plt.title(f"Pie Chart: {col}")
            plt.tight_layout()
            plt.show()

        elif choice == "5":
            col = input("Enter column name for Histogram: ").strip()
            plt.figure(figsize=(10, 6))
            self.data[col].plot(kind="hist", bins=20, color="mediumseagreen", edgecolor="black")
            plt.title(f"Histogram: {col}")
            plt.tight_layout()
            plt.show()

        elif choice == "6":
            plt.figure(figsize=(12, 8))
            sns.heatmap(self.data[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            plt.show()

        elif choice == "7":
            x_col = input("Enter x-axis column name: ").strip()
            y_cols = [c.strip() for c in input("Enter y-axis column names (comma-separated): ").split(",")]
            plt.figure(figsize=(10, 6))
            plt.stackplot(self.data[x_col], [self.data[c] for c in y_cols], labels=y_cols)
            plt.legend(loc="upper left")
            plt.title("Stack Plot")
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid choice.")

    def visualize_seaborn(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Seaborn Visualization ---")
        print("1. Boxplot\n2. Violin Plot\n3. Bar Chart (Seaborn)")
        choice = input("Enter your choice: ").strip()
        if choice in ("1", "2", "3"):
            x_col = input("Enter x-axis column name: ").strip()
            y_col = input("Enter y-axis column name: ").strip()
            plt.figure(figsize=(10, 6))
            if choice == "1":
                sns.boxplot(x=self.data[x_col], y=self.data[y_col])
            elif choice == "2":
                sns.violinplot(x=self.data[x_col], y=self.data[y_col])
            elif choice == "3":
                sns.barplot(x=self.data[x_col], y=self.data[y_col])
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid choice.")

    def multiple_plots(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            print("No numeric columns.")
            return
        cols_to_plot = numeric_cols[:3]
        fig, axes = plt.subplots(1, len(cols_to_plot), figsize=(16, 5))
        if len(cols_to_plot) == 1:
            axes = [axes]
        for i, col in enumerate(cols_to_plot):
            axes[i].hist(self.data[col], bins=15, color="skyblue", edgecolor="black")
            axes[i].set_title(col)
        plt.tight_layout()
        plt.show()

    def save_visualization(self, filepath):
        if self.data is None:
            print("No dataset loaded.")
            return
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            print("No numeric columns to plot.")
            return
        plt.figure(figsize=(10, 6))
        self.data[numeric_cols[0]].plot(kind="hist", bins=20, color="steelblue", edgecolor="black")
        plt.title(f"Histogram: {numeric_cols[0]}")
        plt.savefig(filepath)
        plt.close()
        print(f"Visualization saved in {filepath} successfully!")

    def handle_missing(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Handle Missing Data ---")
        missing = self.data.isnull().sum()
        if missing.sum() == 0:
            print("No missing values found in the dataset!")
            return
        print(missing[missing > 0])
        print("1. Display rows with missing values")
        print("2. Fill missing values")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print(self.data[self.data.isnull().any(axis=1)])
        elif choice == "2":
            col = input("Enter column name to fill: ").strip()
            val = input("Enter fill value: ").strip()
            try:
                val = float(val)
            except ValueError:
                pass
            self.data[col].fillna(val, inplace=True)
            print("Missing values filled.")
        elif choice == "3":
            self.data.dropna(inplace=True)
            self.data.reset_index(drop=True, inplace=True)
            print("Rows with missing values dropped.")
        elif choice == "4":
            col = input("Enter column name: ").strip()
            val = input("Enter replacement value: ").strip()
            try:
                val = float(val)
            except ValueError:
                pass
            self.data[col].replace(np.nan, val, inplace=True)
            print("Missing values replaced.")
        else:
            print("Invalid choice.")

    def descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Descriptive Statistics ---")
        print(self.data.describe(include="all"))
        print(f"\nSkewness:\n{self.data.select_dtypes(include=[np.number]).skew()}")
        print(f"\nVariance:\n{self.data.select_dtypes(include=[np.number]).var()}")
        print(f"\nPercentiles (25%, 50%, 75%):\n{self.data.select_dtypes(include=[np.number]).quantile([0.25, 0.5, 0.75])}")


def _generate_synthetic_dataset(filepath="data/sales_data.csv"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    np.random.seed(42)
    n = 200
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    regions = ["North", "South", "East", "West", "Central"]
    df = pd.DataFrame({
        "SalesID": range(1, n + 1),
        "Product": np.random.choice(products, n),
        "Region": np.random.choice(regions, n),
        "Sales": np.random.randint(100, 1000, n),
        "Year": np.random.choice([2021, 2022, 2023], n),
    })
    df.to_csv(filepath, index=False)
    return filepath


def main():
    sdf = SalesDataFrame()
    while True:
        print("\n========== Data Analytic & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 58)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n-- Load Dataset --")
            DEFAULT_PATH = "data/sales_data.csv"
            path = input(f"Enter the path of the dataset (CSV file) [default: {DEFAULT_PATH}]: ").strip()
            full_path = path if path else DEFAULT_PATH
            if not os.path.exists(full_path):
                print(f"File not found at '{full_path}'. Generating synthetic dataset...")
                full_path = _generate_synthetic_dataset(full_path)
            try:
                sdf.load(full_path)
            except Exception as e:
                print(f"Error loading dataset: {e}")

        elif choice == "2":
            sdf.explore()

        elif choice == "3":
            print("\n-- DataFrame Operations --")
            print("1. Mathematical Operations")
            print("2. Combine DataFrames")
            print("3. Split DataFrame")
            print("4. Search / Sort / Filter")
            sub = input("Enter your choice: ").strip()
            if sub == "1":
                sdf.mathematical()
            elif sub == "2":
                other_path = input("Enter path of second CSV to merge: data/").strip()
                other = SalesDataFrame()
                try:
                    other.load(f"data/{other_path}")
                    on_col = input("Enter column to merge on (or press Enter to concat): ").strip()
                    result = sdf.combine(other, on=on_col if on_col else None)
                    print(result.head())
                except Exception as e:
                    print(f"Error: {e}")
            elif sub == "3":
                col = input("Enter column to split on (or press Enter for equal split): ").strip()
                val = input("Enter value to split by (or press Enter to skip): ").strip()
                part1, part2 = sdf.split(col=col if col else None, value=val if val else None)
                print(f"Part 1: {len(part1)} rows | Part 2: {len(part2)} rows")
            elif sub == "4":
                col = input("Enter column to search/sort/filter: ").strip()
                val = input("Enter value to search (or press Enter to skip): ").strip()
                result = sdf.search_sort(col=col, value=val if val else None)
                print(result.head(10))
            else:
                print("Invalid choice.")

        elif choice == "4":
            sdf.handle_missing()

        elif choice == "5":
            sdf.descriptive_statistics()

        elif choice == "6":
            print("\n-- Data Visualization --")
            print("1. Matplotlib Visualization")
            print("2. Seaborn Visualization")
            print("3. Multiple Plots")
            sub = input("Enter your choice: ").strip()
            if sub == "1":
                sdf.visualize_data()
            elif sub == "2":
                sdf.visualize_seaborn()
            elif sub == "3":
                sdf.multiple_plots()
            else:
                print("Invalid choice.")

        elif choice == "7":
            print("\n-- Save Visualization --")
            fname = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip()
            sdf.save_visualization(fname)

        elif choice == "8":
            print("Exiting the program. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
