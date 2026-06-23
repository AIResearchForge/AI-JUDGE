"""Utility functions for AI Judge."""

import re
from typing import List, Dict, Any


def extract_truth_score(text: str) -> int:
    """Extracts Truth Score from the agent's response."""

    match = re.search(r"Truth Score:\s*(\d+)%", text)
    if match:
        return int(match.group(1))
    return 0


def count_stars(text: str) -> int:
    """Counts filled stars (★) in the response."""

    match = re.search(r"Credibility:\s*([★☆]+)", text)
    if match:
        return match.group(1).count("★")
    return 0


def calculate_stars(truth_score: int) -> str:
    """Calculates the number of stars based on Truth Score."""

    if truth_score == 0:
        return "☆☆☆☆☆"
    elif truth_score <= 19:
        return "★☆☆☆☆"
    elif truth_score <= 49:
        return "★★☆☆☆"
    elif truth_score <= 69:
        return "★★★☆☆"
    elif truth_score <= 89:
        return "★★★★☆"
    else:
        return "★★★★★"


def format_report(truth_score: int, reasons: List[str]) -> str:
    """Creates a formatted report with the evaluation."""

    stars = calculate_stars(truth_score)

    report = f"Truth Score: {truth_score}%\n"
    report += f"Credibility: {stars}\n"
    report += "Reasons:\n"
    for reason in reasons:
        report += f"✓ {reason}\n"

    return report


def parse_scoring_response(text: str) -> Dict[str, Any]:
    """Parses Agent 3's response into a dictionary."""

    truth_score = extract_truth_score(text)
    stars_count = count_stars(text)

    reasons = []
    if "Reasons:" in text:
        parts = text.split("Reasons:")[1].strip()
        for line in parts.split("\n"):
            line = line.strip()
            if line.startswith("✓"):
                reasons.append(line[1:].strip())

    if not reasons:
        reasons = ["No reasons provided."]

    return {
        "truth_score": truth_score,
        "stars": stars_count,
        "stars_text": calculate_stars(truth_score),
        "reasons": reasons,
    }


__all__ = [
    "extract_truth_score",
    "count_stars",
    "calculate_stars",
    "format_report",
    "parse_scoring_response",
]
