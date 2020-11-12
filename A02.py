squares = [x**2 for x in range(0, 51)]
cubes = [x**3 for x in range(20, 31)]
funcValues = [3*x - 2 for x in range(-5, 6)]
numPairs = [(x, y) for x in range(10, 21) for y in range(5, 11)]
numWordPairs = [(x, y) for x in range(4, 8) for y in ["jabłko", "gruszka", "komputer"]]

print(squares)
print(cubes)
print(funcValues)
print(numPairs)
print(numWordPairs)
