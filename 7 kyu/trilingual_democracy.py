def trilingual_democracy(group):
    from collections import Counter

    all_languages = {'D', 'F', 'I', 'K'}

    counts = Counter(group)

    if len(counts) == 1:
        return group[0]

    if len(counts) == 2:
        for language, count in counts.items():
            if count == 1:
                return language

    if len(counts) == 3:
        return (all_languages - set(group)).pop()
