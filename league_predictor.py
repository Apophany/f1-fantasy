import cvxpy as cp
import numpy as np

import ranking_model as models
import data.costs.constructor_costs as cc
import data.costs.driver_costs as dc


def run_model(budget, model, model_name, excluded_drivers, excluded_constructors):
    driver_costs = dict(dc.driver_costs)
    constructor_costs = dict(cc.constructor_costs)

    for driver in excluded_drivers:
        driver_costs.pop(driver)
        model.pop(driver)

    for constructor in excluded_constructors:
        constructor_costs.pop(constructor)
        model.pop(constructor)

    driver_count = 20 - len(excluded_drivers)
    constructor_count = 10 - len(excluded_constructors)

    # Is pick i a driver
    driver = np.append(np.ones(driver_count), np.zeros(constructor_count))

    # Is pick i a constructor
    constructor = np.append(np.zeros(driver_count), np.ones(constructor_count))

    # How much does pick i cost
    costs = np.array(list(driver_costs.values()) + list(constructor_costs.values()))

    result = 0

    # We can choose one driver < $20mil to score double points, so run the model for each
    for i in range(0, len(costs)):
        tmp_values = list(model.values()).copy()
        if costs[i] < 20.0 and driver[i] == 1:
            tmp_values[i] = tmp_values[i] * 2

        # Driver picks
        X = cp.Variable(driver_count + constructor_count, boolean=True)

        # Constraints:
        #   1. Team cost can't exceed $100mil
        #   2. Must have 5 drivers
        #   3. Must have one constructor
        cost_constraint = X * costs <= budget
        num_drivers_constraint = X * driver == 5
        num_constructors_constraint = X * constructor == 1

        # Run the optimisation function for our chosen model
        objective = cp.Maximize(X * tmp_values)
        problem = cp.Problem(objective, [num_drivers_constraint, num_constructors_constraint, cost_constraint])
        res = problem.solve(solver=cp.GLPK_MI)
        result = max(result, res)

    # Output the results
    print("Results for: " + model_name)

    print("Total score: " + str(result))
    print("Total cost: " + str(np.sum(X.value * costs)))

    model_names = list(model.keys())
    print("Results: " + str([model_names[i] for i, x in enumerate(X.value) if x == 1]))
    print("")


if __name__ == "__main__":
    exclude_drivers = []
    exclude_constructors = []
    team_budget = 100

    # Get the expectation values for various models
    predicted_points_model = models.get_ranking(model=models.POINTS_PREDICTED)
    cost_model = models.get_ranking(model=models.COST)
    points_2019_model = models.get_ranking(model=models.POINTS_2020)
    points_per_million_model = models.get_ranking(model=models.POINTS_PER_MILLION)
    fantasy_points_2021 = models.get_ranking(model=models.FANTASY_POINTS_2021)

    run_model(team_budget, cost_model, "Cost only", exclude_drivers, exclude_constructors)
    run_model(team_budget, points_per_million_model, "Points per million", exclude_drivers, exclude_constructors)
    run_model(team_budget, fantasy_points_2021, "Fantasy points 2021", exclude_drivers, exclude_constructors)
