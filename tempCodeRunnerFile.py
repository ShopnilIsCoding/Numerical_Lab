def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange Interpolation: Given a set of points (x_i, y_i), find the value of y corresponding to a given x.

    Arguments:
    x_values -- List of x coordinates of the points
    y_values -- List of y coordinates of the points
    x -- The x value for which we want to find the corresponding y value

    Returns:
    y -- The interpolated y value corresponding to the given x
    """
    n = len(x_values)
    y = 0

    for i in range(n):
        
          L = 1  
          for j in range(n):
            if j!=i:
                L*=(x - x_values[j] )/ (x_values[i] - x_values[j])

          y += y_values[i] * L

    return y

x_values = [10, 15, 20]
y_values = [227.04, 362.78, 517.35]
x = 16
y = lagrange_interpolation(x_values, y_values, x)
print(y)

x_values = [10, 15, 16, 20]
y_values = [227.04, 362.78, 392.1875999999999, 517.35]
x = 16



import matplotlib.pyplot as plt

def plot_graph(x_values, y_values):
   plt.plot(x_values, y_values, marker='o', linestyle='-')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.title('Plot of y vs. x')
   plt.grid(True)
   plt.show()

   plot_graph(x_values , y_values )