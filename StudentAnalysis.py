import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

################################################
# 1. Load DataSet and display Basic Information
#################################################

df = pd .read_csv("student_performance_ml.csv")

print("\nFirst 5 records : ")
print(df.head())

print("\n Last 5 records : ")
print(df.tail())

print("\n Dataset Shape(Rows,Columns) : ")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\n Data Types : ")
print(df.dtypes)

################################################
# 2. Total Students,Passed & Failed
#################################################

print("\n Total Students : ", len(df))
print("Total Passed students : ",(df["FinalResult"] == 1) .sum())
print("Total Failed students : ",(df["FinalResult"] == 0) .sum())

################################################
# 3. Statistical Calculations
#################################################

print("\nAverage StudyHours : ", df["StudyHours"].mean())
print("\nAverage Attendance : ", df["Attendance"].mean())

print("\nMaximum PreviousScore : ", df["PreviousScore"].max())
print("\nMinimum SleepHours : ", df["SleepHours"].min())

################################################
# 4. FinalResult Distributions
#################################################

print("\nFinal Result Distribution:")
print(df["FinalResult"].value_counts())

print("\nPercentage Distribution:")
print(df["FinalResult"].value_counts(normalize=True) * 100)

################################################
# 5. Analysis
#################################################

print("\nAverage StudyHours by FinalResult:")
print(df.groupby("FinalResult")["StudyHours"].mean())

print("\nAverage Attendance by FinalResult:")
print(df.groupby("FinalResult")["Attendance"].mean())

################################################
# 6. Histogram of StudyHours
#################################################

plt.figure()
plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

################################################
# 7. Scatter Plot: StudyHours vs PreviousScore
#################################################

# Colored Scatter Plot
plt.figure()
sns.scatterplot(x="StudyHours",
                y="PreviousScore",
                hue="FinalResult",
                data=df)
plt.title("StudyHours vs PreviousScore (Pass/Fail)")
plt.show()

################################################
# 8. BoxPlot For Attendance
#################################################

plt.figure()
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.show()

################################################
# 9. AssignmentsCompleted And FinalResult
#################################################

plt.figure()
sns.boxplot(x="FinalResult",
            y="AssignmentsCompleted",
            data=df)
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()

################################################
# 10. SleepHours And FinalResult
#################################################

plt.figure()
sns.boxplot(x="FinalResult",
            y="SleepHours",
            data=df)
plt.title("SleepHours vs FinalResult")
plt.show()

