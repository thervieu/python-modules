from vector import Vector

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([0.0, 1.0, 2.0, 3.0])

print("v1:", str(v1), "\n")

print("v1 + 3:", str(v1 + 3))
print("3 + v1:", str(3 + v1), "\n")

print("v1 - 2:", str(v1 - 2))
print("2 - v1:", str(2 - v1), "\n")

print("v1 * 3:", str(v1 * 3))
print("3 * v1:", str(3 * v1), "\n")

print("v1 / 2:", str(v1 / 2), "\n")
# print("3 / v1:", str(3 / v1), "\n")

print("v1 + v1:", str(v1 + v1))
print("v1 - v1:", str(v1 - v1), "\n")
print("v1.dot(v1):", str(v1.dot(v1)), "\n\n")


print("v2:", str(v2), "\n")

print("v2 + 3:", str(v2 + 3))
print("3 + v2:", str(3 + v2), "\n")

print("v2 - 2:", str(v2 - 2))
print("2 - v2:", str(2 - v2), "\n")

print("v2 * 3:", str(v2 * 3))
print("3 * v2:", str(3 * v2), "\n")

print("v2 / 2:", str(v2 / 2), "\n")
# print("3 / v2:", str(3 / v2), "\n")
print("v2.dot(v2):", str(v2.dot(v2)), "\n\n")

print("v2 + v2:", str(v2 + v2))
print("v2 - v2:", str(v2 - v2), "\n\n")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("v_col shape", str(v1.shape))
print("v_col transpose", str(v1.T()))
print("v_col transpose shape", v1.T().shape, "\n\n")

v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v_line shape", str(v2.shape))
print("v_line transpose", str(v2.T()))
print("v_line transpose shape", v2.T().shape)