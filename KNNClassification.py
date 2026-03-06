import math
def knn_classification():
    dataset = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue")
    ]
# User input
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    distances = []
# Calculate Euclidean Distance
    for point in dataset:
        name, x1, y1, label = point
        distance = math.sqrt((x - x1)**2 + (y - y1)**2)
        distances.append((name, distance, label))

# Sort distances
    distances.sort(key=lambda d: d[1])

    print("\nNearest Neighbors:")
    for i in range(3):
        print(distances[i][0], "- Distance:", round(distances[i][1],2))

# Majority voting (K=3)
    red = 0
    blue = 0

    for i in range(3):
        if distances[i][2] == "Red":
            red = red + 1
        else:
            blue = blue + 1

    if red > blue:
        print("\nPredicted Class: Red")
    else:
        print("\nPredicted Class: Blue")

    print("\nPrediction Results for Different K:")


# 2. Show prediction for K=1,3,5

    for k in [1,3,4]:
        red = 0
        blue = 0

        for i in range(k):
            if distances[i][2] == "Red":
                red += 1
            else:
                blue += 1

        result = "Red" if red > blue else "Blue"
        print("K =", k, "->", result)
def main():
    knn_classification()

if __name__ == "__main__":
    main()