import math

def student_result_knn():

    dataset = [
        (2,60,"Fail"),
        (5,80,"Pass"),
        (6,85,"Pass"),
        (1,50,"Fail")
    ]

    study = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))

    distances = []

    for data in dataset:
        h, a, result = data
        distance = math.sqrt((study - h)**2 + (attendance - a)**2)
        distances.append((distance, result))

    distances.sort()

    k = 3
    pass_count = 0
    fail_count = 0

    for i in range(k):
        if distances[i][1] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    if pass_count > fail_count:
        print("\nPredicted Result: Pass")
    else:
        print("\nPredicted Result: Fail")
def main():
    student_result_knn()

if __name__ == "__main__":
    main()