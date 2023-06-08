def study_schedule(permanence_period, target_time):
    if not permanence_period or target_time is None:
        return None

    count = 0
    for period in permanence_period:
        start_time, end_time = period
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        if start_time <= target_time and end_time >= target_time:
            count += 1

    return count

    raise NotImplementedError
