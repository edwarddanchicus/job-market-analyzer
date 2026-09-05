import re

import pandas as pd

from config import SKILLS


def extract_skills(text: str) -> list[str]:
    text = str(text).lower()
    found = []

    for skill, keywords in SKILLS.items():
        for keyword in keywords:
            pattern = r"(?<!\\w)" + re.escape(keyword.lower()) + r"(?!\\w)"
            if re.search(pattern, text):
                found.append(skill)
                break

    return found


def add_skills_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    combined_text = (
        df["title"].fillna("").astype(str)
        + " "
        + df["description"].fillna("").astype(str)
    )

    df["skills"] = combined_text.apply(extract_skills)
    return df


def skill_statistics(df: pd.DataFrame) -> pd.DataFrame:
    counts = {}

    for skills in df["skills"]:
        for skill in skills:
            counts[skill] = counts.get(skill, 0) + 1

    result = pd.DataFrame(
        [{"skill": skill, "count": count} for skill, count in counts.items()]
    )

    if result.empty:
        return pd.DataFrame(columns=["skill", "count"])

    return result.sort_values("count", ascending=False).reset_index(drop=True)
