def diamond(n):
	if n % 2 == 0 or n < 0: return None
	x = 1
	result = ""
	for f in range(0, n):
		spaces = (n - x) / 2
		result += (" " * spaces) + ("*" * x) + "\n"
		if f < n / 2:
			x+=2
		else:
			x-=2
	return result

print(diamond(1))
print(diamond(0))
print(diamond(5))
print(diamond(15))
print(diamond(26))
