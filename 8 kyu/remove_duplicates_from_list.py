def distinct(seq):
    seen = set()
    result = []

    for number in seq:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result