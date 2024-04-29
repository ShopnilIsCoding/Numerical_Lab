def f(x):
    return x**2
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    total_area = 0.5 * (f(a) + f(b)) 
    for i in range(1, n):
        total_area += f(a + i * h)
    return total_area * h
a = 0  
b = 12  
n = 6
total_area = trapezoidal_rule(a, b, n)

print("Total area covered by the graph:", total_area)