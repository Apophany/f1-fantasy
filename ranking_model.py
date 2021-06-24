import numpy as np

import data.points.points_2019 as _2018
import data.points.points_2020 as _2019
import data.points.points_predicted as _predicted
import data.points.points_per_million as _per_million
import data.points.fantasy_points_2021 as _fantasy_points_2021
from data.costs.constructor_costs import *
from data.costs.driver_costs import *

PLACEMENT = "placement"
COST = "cost"
POINTS_2019 = "points_2019"
POINTS_2020 = "points_2020"
POINTS_PREDICTED = "points_predicted"
POINTS_PER_MILLION = "points_per_million"
FANTASY_POINTS_2021 = "fantasy_points_2021"


def get_ranking(model):
    models = {
        COST: __cost_model(),
        PLACEMENT: __placement_ranking(),
        POINTS_2019: __points_2019(),
        POINTS_2020: __points_2020(),
        POINTS_PREDICTED: __points_predicted(),
        POINTS_PER_MILLION: __points_per_million(),
        FANTASY_POINTS_2021: __fantasy_points_2021()
    }
    return models.get(model, lambda: "Invalid model")


def __cost_model():
    combined_costs = dict(driver_costs)
    combined_costs.update(constructor_costs)
    return combined_costs


def __placement_ranking():
    driver_ranking = np.arange(1, 21, 1)
    constructor_ranking = np.arange(1, 11, 1)
    driver_ranking[::-1].sort()
    constructor_ranking[::-1].sort()

    return np.append(driver_ranking, constructor_ranking)


def __points_per_million():
    return _per_million.points


def __points_2019():
    return _2018.points


def __points_2020():
    return _2019.points


def __points_predicted():
    return _predicted.points


def __fantasy_points_2021():
    return _fantasy_points_2021.points
