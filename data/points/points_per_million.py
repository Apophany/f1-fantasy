import numpy as np

import data.points.fantasy_points_2021
from data.costs.constructor_costs import constructor_costs
from data.costs.driver_costs import driver_costs

points = {
    'Hamilton': 7.552870090634441,
    'Verstappen': 10.7421875,
    'Bottas': 4.826086956521739,
    'Perez': 10.268817204301074,
    'Ricciardo': 6.7924528301886795,
    'Leclerc': 7.078651685393258,
    'Vettel': 6.622516556291391,
    'Alonso': 4.594594594594595,
    'Sainz': 7.054794520547945,
    'Stroll': 3.6842105263157894,
    'Norris': 15.179856115107913,
    'Gasly': 10.59322033898305,
    'Ocon': 5.0,
    'Raikkonen': 5.913978494623655,
    'Tsunoda': 3.6904761904761902,
    'Giovinazzi': 6.0,
    'Latifi': 1.71875,
    'Russell': 5.967741935483871,
    'Schumacher': 10.172413793103448,
    'Mazepin': 3.9622641509433962,

    'Mercedes': 8.739946380697052,
    'Ferrari': 10.736842105263158,
    'Red Bull': 15.378787878787879,
    'Alpine': 7.516339869281046,
    'Aston Martin': 8.475609756097562,
    'Alfa Romeo': 9.56521739130435,
    'Haas': 10.655737704918034,
    'McLaren': 14.999999999999998,
    'Alpha Tauri': 10.793650793650794,
    'Williams': 7.301587301587301
}

if __name__ == "__main__":
    names = np.array(list(driver_costs.keys()) + list(constructor_costs.keys()))
    costs = np.array(list(driver_costs.values()) + list(constructor_costs.values()))
    points = np.array(list(data.points.fantasy_points_2021.points.values()))

    points_per_million = points / costs

    results = {}
    for A, B in zip(names, points_per_million):
        results[A] = B

    print(results)
