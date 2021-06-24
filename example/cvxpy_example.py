import numpy as np
from matplotlib import pyplot as plt
from cvxpy import *

if __name__ == "__main__":
    np.random.seed(1)
    n = 8
    m = 2
    T = 50
    alpha = 0.2
    beta = 5
    A = np.eye(n) + alpha * np.random.randn(n, n)
    B = np.random.randn(n, m)
    x_0 = beta * np.random.randn(n)

    x = Variable((n, T + 1))
    u = Variable((m, T))

    cost = 0
    constr = []
    for t in range(T):
        cost += sum_squares(x[:, t + 1]) + sum_squares(u[:, t])
        constr += [x[:, t + 1] == A * x[:, t] + B * u[:, t],
                   norm(u[:, t], 'inf') <= 1]
    # sums problem objectives and concatenates constraints.
    constr += [x[:, T] == 0, x[:, 0] == x_0]
    problem = Problem(Minimize(cost), constr)
    print(problem.solve(solver='ECOS'))

    f = plt.figure()

    # Plot (u_t)_1.
    ax = f.add_subplot(411)
    plt.plot(u[0,:].value)
    plt.ylabel(r"$(u_t)_1$", fontsize=16)
    plt.yticks(np.linspace(-1.0, 1.0, 3))
    plt.xticks([])

    # Plot (u_t)_2.
    plt.subplot(4,1,2)
    plt.plot(u[1,:].value)
    plt.ylabel(r"$(u_t)_2$", fontsize=16)
    plt.yticks(np.linspace(-1, 1, 3))
    plt.xticks([])

    # Plot (x_t)_1.
    plt.subplot(4,1,3)
    x1 = x[0,:].value
    plt.plot(x1)
    plt.ylabel(r"$(x_t)_1$", fontsize=16)
    plt.yticks([-10, 0, 10])
    plt.ylim([-10, 10])
    plt.xticks([])

    # Plot (x_t)_2.
    plt.subplot(4,1,4)
    x2 = x[1,:].value
    plt.plot(range(51), x2)
    plt.yticks([-25, 0, 25])
    plt.ylim([-25, 25])
    plt.ylabel(r"$(x_t)_2$", fontsize=16)
    plt.xlabel(r"$t$", fontsize=16)
    plt.tight_layout()
    plt.show()