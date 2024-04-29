def divided_difference(times, values, start, end):
    if start == end:
        return values[start]
    else:
        numerator = divided_difference(times, values, start + 1, end) - divided_difference(times, values, start, end - 1)
        denominator = times[end] - times[start]
        return numerator / denominator

def newton_divided_difference_interpolation(t, times, values):
    n = len(times)
    result = 0.0
    product_term = 1.0
    
    for i in range(n):
        divided_diff = divided_difference(times, values, 0, i)
        result += divided_diff * product_term
        if i < n - 1:
            product_term *= (t - times[i])
    
    return result
times = input("Enter the list of time points : ").split(",")
times = [float(time) for time in times]
values = input("Enter the corresponding list of values : ").split(",")
values = [float(value) for value in values]
t = 16 
interpolated_value = newton_divided_difference_interpolation(t, times, values)
print(f"The interpolated value at time {t} is {interpolated_value}")
