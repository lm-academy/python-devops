from typing import TypedDict
import re


class TextAttributes(TypedDict):
    word_count: int
    unique_words: set[str]
    average_word_length: float
    longest_word: str


def calculate_text_attributes(input_text: str) -> TextAttributes:
    split_text = re.findall(r"\w+", input_text)
    word_length_sum = sum(len(word) for word in split_text)
    avg_word_length = (
        word_length_sum / len(split_text)
        if len(split_text)
        else 0
    )

    return {
        "word_count": len(split_text),
        "unique_words": set(text.lower() for text in split_text),
        "average_word_length": avg_word_length,
        "longest_word": (
            max(split_text, key=len) if split_text else ""
        ),
    }
