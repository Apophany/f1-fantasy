def calculate_points(results):
    pass


def __finished_race(driver_laps, winner_laps):
    # Need to have completed 90% of winners laps to be classified as finished
    return driver_laps / winner_laps < 0.9
