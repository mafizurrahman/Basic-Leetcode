import itertools

# Define a list of points (x, y)
points = [(1, 2), (3, 10), (5, 6), (7, 8), (9, 10)]
new = []
# Calculate the area of triangles for all combinations of three points
for combo in itertools.combinations(points, 3):
    (x1, y1), (x2, y2), (x3, y3) = combo
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    # print(f"Triangle with points {combo}: Area = {area}")
    new.append(area)

print(max(new))