# Simple example to show Gradient Descent for simple arrays
# The number of iterations and the learning rate can be adjusted.

from matplotlib import pyplot as plt

# Sample points
x_points = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y_points = [2, 3, 5, 6, 2, 7, 8, 9, 3, 10, 12, 9]

# Define global m and b values
m = 0
b = 0

# Define the Line equation in terms of y = mx + b
y = lambda x: m * x + b

# Plot the line based on Gradient descent equation.
def line_plot(y_value, data_points):
    x_values = [i for i in range(int(min(data_points)) - 1, int(max(data_points)) + 2)]
    y_values = [y(x) for x in x_values]
    plt.plot(x_values, y_values, "r")

# Compute summation for m and b.
def find_line_by_summation(y, x_points, y_points):
    sum1 = 0
    sum2 = 0

    # Adding the values as per Gradient Descent Equations.
    for i in range(1, len(x_points)):
        # Computing part of m (In y = mx + b)
        sum1 += y(x_points[i]) - y_points[i]

        # Computing part of b (In y = mx + b)
        sum2 += (y(x_points[i]) - y_points[i]) * x_points[i]

    # Dividing by the total number of points.
    return sum1 / len(x_points), sum2 / len(x_points)

# Call the line function as many times by changing number of iterations.
# Varying the number of iterations and learn rate can demonstrate changes in the fit.
if __name__ == "__main__":
    iterations = 50
    learn_rate = .001

    # Add summations to m and b for final m and b values.
    for i in range(iterations):
        sum1, sum2 = find_line_by_summation(y, x_points, y_points)
        m = m - learn_rate * sum2
        b = b - learn_rate * sum1

    print("m_value : ", m)
    print("b_value : ", b)

    line_plot(y, x_points)
    plt.plot(x_points, y_points, 'bo')
    plt.show()