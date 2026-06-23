"""Example questions for AI Judge tests."""

from pathlib import Path

EXAMPLE_QUESTIONS_FILE = Path(__file__).parent / "example_questions.txt"


def load_example_questions() -> list[str]:
    """Loads example questions from file."""

    if not EXAMPLE_QUESTIONS_FILE.exists():
        return [
            "Was the COVID vaccine created by Polish scientists?",
            "Are climate changes caused by humans?",
            "Did Elon Musk invent the Internet?",
            "Is the Moon made of cheese?",
            "Does 5G cause cancer?",
        ]

    with open(EXAMPLE_QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


__all__ = ["load_example_questions"]
