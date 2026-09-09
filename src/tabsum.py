"""Summarize count= fields in newline-delimited metric logs."""
from collections import Counter


def summarize(lines):
    counts = Counter()
    for line in lines:
        for token in line.split():
            if token.startswith("count="):
                try:
                    counts[token[len("count="):]] += int(token[len("count="):])
                except ValueError:
                    continue
    return dict(counts)


def summarize_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return summarize(handle)
