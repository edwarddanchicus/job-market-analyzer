import argparse
import json
from pathlib import Path

import pandas as pd

from config import DATA_DIR, DEFAULT_SOURCE_URL, RESULTS_DIR, TOP_N
from collectors.jobs_api import fetch_jobs
from analysis.skills import add_skills_column, skill_statistics
from analysis.statistics import save_bar_chart, top_counts


def normalize_jobs(raw_jobs: list[dict]) -> pd.DataFrame:
    rows = []

    field_aliases = {
        "title": ["title", "job_title", "name", "stellenangebotsTitel"],
        "company": ["company", "employer", "company_name", "arbeitgeber"],
        "location": ["location", "city", "place", "arbeitsort"],
        "description": [
            "description",
            "job_description",
            "content",
            "stellenangebotsBeschreibung",
        ],
        "url": ["url", "link", "job_url", "externeUrl"],
    }

    for job in raw_jobs:
        row = {}

        for target, aliases in field_aliases.items():
            value = ""
            for alias in aliases:
                if alias in job and job[alias] is not None:
                    value = job[alias]
                    break
            row[target] = str(value)

        rows.append(row)

    return pd.DataFrame(
        rows,
        columns=["title", "company", "location", "description", "url"],
    )


def sample_jobs() -> list[dict]:
    return [
        {
            "title": "Junior Python Developer",
            "company": "Example Tech",
            "location": "Dortmund",
            "description": "Python, SQL, Git and Docker experience.",
        },
        {
            "title": "IT System Administrator",
            "company": "Example Systems",
            "location": "Dortmund",
            "description": "Linux, networking, Windows Server and PowerShell.",
        },
        {
            "title": "Cloud Engineer",
            "company": "Example Cloud",
            "location": "Berlin",
            "description": "AWS, Docker, Kubernetes and Python.",
        },
        {
            "title": "Cybersecurity Analyst",
            "company": "Example Security",
            "location": "Cologne",
            "description": "Cybersecurity, Linux, networking and Python.",
        },
    ]


def run_pipeline(raw_jobs: list[dict]):
    DATA_DIR.mkdir(exist_ok=True)
    RESULTS_DIR.mkdir(exist_ok=True)

    raw_path = DATA_DIR / "raw_jobs.json"
    cleaned_path = DATA_DIR / "cleaned_jobs.csv"

    with open(raw_path, "w", encoding="utf-8") as file:
        json.dump(raw_jobs, file, indent=2, ensure_ascii=False)

    df = normalize_jobs(raw_jobs)

    if df.empty:
        raise RuntimeError("No job listings were available for analysis.")

    df = add_skills_column(df)
    df["skills"] = df["skills"].apply(lambda values: ", ".join(values))

    df.to_csv(cleaned_path, index=False)

    # Convert the comma-separated skills back to lists for statistics.
    analysis_df = df.copy()
    analysis_df["skills"] = analysis_df["skills"].apply(
        lambda value: [item.strip() for item in value.split(",") if item.strip()]
    )

    skills_df = skill_statistics(analysis_df)
    skills_df.to_csv(RESULTS_DIR / "skill_demand.csv", index=False)

    locations_df = top_counts(df, "location", TOP_N)
    titles_df = top_counts(df, "title", TOP_N)

    locations_df.to_csv(RESULTS_DIR / "top_locations.csv", index=False)
    titles_df.to_csv(RESULTS_DIR / "top_job_titles.csv", index=False)

    save_bar_chart(
        skills_df.head(TOP_N),
        "skill",
        "count",
        "Most In-Demand Technical Skills",
        RESULTS_DIR / "top_skills.png",
    )

    save_bar_chart(
        locations_df,
        "location",
        "count",
        "Top Job Locations",
        RESULTS_DIR / "top_locations.png",
    )

    save_bar_chart(
        titles_df,
        "title",
        "count",
        "Most Common Job Titles",
        RESULTS_DIR / "top_job_titles.png",
    )

    print("\nJob Market Analysis Complete")
    print("=" * 35)
    print(f"Jobs analyzed: {len(df)}")

    if not skills_df.empty:
        print("\nTop technical skills:")
        for index, row in skills_df.head(10).iterrows():
            print(f"{index + 1}. {row['skill']}: {row['count']}")

    print(f"\nResults saved to: {RESULTS_DIR}")


def main():
    parser = argparse.ArgumentParser(
        description="Collect and analyze job market data."
    )

    parser.add_argument(
        "--source-url",
        help="Public JSON endpoint containing job listings.",
    )

    parser.add_argument(
        "--sample-data",
        action="store_true",
        help="Run the analysis using built-in sample data.",
    )

    args = parser.parse_args()

    if args.sample_data:
        print("Using built-in sample job data...")
        raw_jobs = sample_jobs()
    else:
        source_url = args.source_url or DEFAULT_SOURCE_URL

        if not source_url:
            parser.error(
                "Provide --source-url or use --sample-data."
            )

        print(f"Collecting job data from: {source_url}")
        raw_jobs = fetch_jobs(source_url)

    run_pipeline(raw_jobs)


if __name__ == "__main__":
    main()
