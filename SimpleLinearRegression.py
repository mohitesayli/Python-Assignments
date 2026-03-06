import numpy as np
import  matplotlib.pyplot as plt 

def linear_Regression():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("Mean of X :", mean_X)
    print("Mean of Y :", mean_Y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_X) * (Y[i] - mean_Y)
        denominator += (X[i] - mean_X) ** 2

    m = numerator / denominator
    C = mean_Y - (m * mean_X)

    print("Slope (m) :", m)
    print("Intercept (C) :", C)

    print("Regression Equation: Y =", m, "X +", C)

# Predict for X = 6
    predicted = m * 6 + C
    print("Predicted Y for X = 6 :", predicted)

    return X, Y, m, C

# 2. Calculate Model Performance

def evaluate_model_performance(X, Y, m, C):

    n = len(X)
    mean_Y = np.mean(Y)

    ss_res = 0
    ss_tot = 0

    print("\nPredicted Values:")

    for i in range(n):
        Yp = m * X[i] + C
        print(f"X = {X[i]}  Predicted Y = {Yp}")

        ss_res += (Y[i] - Yp) ** 2
        ss_tot += (Y[i] - mean_Y) ** 2

    MSE = ss_res / n
    R_square = 1 - (ss_res / ss_tot)

    print("\nMSE :", MSE)
    print("R-Square :", R_square)

# 3. Salary Prediction Model

def salary_prediction_model():
    experience = [1,2,3,4,5]
    salary = [20000,25000,30000,35000,40000]

    mean_X = np.mean(experience)
    mean_Y = np.mean(salary)

    n = len(experience)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (experience[i] - mean_X) * (salary[i] - mean_Y)
        denominator += (experience[i] - mean_X) ** 2

        m = numerator / denominator
    C = mean_Y - (m * mean_X)

    print("\nSalary Regression Equation: Y =", m, "X +", C)

    predicted_salary = m * 6 + C
    print("Predicted Salary for 6 Years Experience :", predicted_salary)

# Plot Graph
    x_line = np.linspace(1,6,100)
    y_line = m * x_line + C

    plt.scatter(experience, salary)
    plt.plot(x_line, y_line)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Salary vs Experience Regression Line")
    plt.show()

def main():
    X, Y, m, C = linear_Regression()
    evaluate_model_performance(X, Y, m, C)
    salary_prediction_model()

if __name__ == "__main__":
    main()