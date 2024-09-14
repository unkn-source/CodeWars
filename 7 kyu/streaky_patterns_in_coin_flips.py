def check_sequence(sequence, l, n):
    streak_count = 0
    current_streak_char = None
    current_streak_len = 0

    for char in sequence:
        if char == current_streak_char:
            current_streak_len += 1
        else:
            if current_streak_len == l:
                streak_count += 1

            current_streak_char = char
            current_streak_len = 1

        if streak_count > n:
            return False

    if current_streak_len == l:
        streak_count += 1

    return streak_count == n