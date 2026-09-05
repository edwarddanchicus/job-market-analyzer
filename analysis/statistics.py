import pandas as pd
import matplotlib.pyplot as plt


def top_counts(df: pd.DataFrame, column: str, top_n: int) -> pd.DataFrame:
    series = (
        df[column]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace("", "Unknown")
        .value_counts()
        .head(top_n)
    )

    return series.rename_axis(column).reset_index(name="count")


def save_bar_chart(
    data: pd.DataFrame,
    label_column: str,
    value_column: str,
    title: str,
    output_path,
):
    if data.empty:
        return

    plt.figure(figsize=(10, 6))
    plt.barh(data[label_column].astype(str), data[value_column])
    plt.xlabel("Number of job listings")
    plt.ylabel(label_column.replace("_", " ").title())
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
