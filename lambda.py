def build_quadratic_function(a, b, c):
	return lambda x: a * (x ** 2) + b * x + c

f = build_quadratic_function(2, 3, -5)

f(0)