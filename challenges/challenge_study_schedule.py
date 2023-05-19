def study_schedule(permanence_period, target_time):
    if (
        target_time is None
        or not permanence_period
        or not all(
            isinstance(start, int) and isinstance(end, int) and start <= end
            for start, end in permanence_period
        )
    ):
        return None

    count = sum(
        1 for start, end in permanence_period if start <= target_time <= end
    )
    return count
