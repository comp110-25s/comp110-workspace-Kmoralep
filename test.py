def reverse(original: list[str]) -> list[str]:
    idx: int = len(original)
    results: list[str] = []
    while idx > 0:
        idx = idx - 1
        results.append(original[idx])
    return results
