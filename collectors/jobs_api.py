import time
from typing import Any

import requests

from config import MAX_RETRIES, REQUEST_TIMEOUT


def _extract_jobs(payload: Any) -> list[dict]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]

    if isinstance(payload, dict):
        for key in ("jobs", "data", "results", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]

    raise ValueError(
        "Could not find a list of jobs. Expected a JSON list or a "
        "dictionary containing jobs/data/results/items."
    )


def fetch_jobs(source_url: str) -> list[dict]:
    headers = {
        "User-Agent": "JobMarketAnalyzer/1.0 (educational portfolio project)"
    }

    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(
                source_url,
                headers=headers,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            return _extract_jobs(response.json())

        except (requests.RequestException, ValueError) as error:
            last_error = error
            if attempt < MAX_RETRIES:
                time.sleep(attempt)

    raise RuntimeError(f"Unable to collect job data: {last_error}")
