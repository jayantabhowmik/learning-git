def my_function(a, b):
    print(a + b)  # Corrected indentation
    return a + b


def unused_function():
    pass  # This function is still unused, but no issue if kept for future use


x = 5
y = 10
z = my_function(x, y)

if z > 10:
    print("Greater than 10")  # Corrected single-line if statement and spacing
