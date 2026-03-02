import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

########################################################
# 2. Load Dataset
########################################################
data = pd.read_csv("student_performance_ml.csv")

print("First 5 Rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

########################################################
# 3. Define Features & Target
########################################################
X = data.drop("FinalResult", axis=1)
y = data["FinalResult"]

########################################################
# 4. Train-Test Split
########################################################
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

########################################################
# 5. Train Decision Tree Model
########################################################
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

########################################################-
# 6. Prediction
########################################################
y_pred = model.predict(X_test)
print("\nActual vs Predicted:")
for a, p in zip(y_test.values, y_pred):
    print("Actual:", a, " Predicted:", p)

########################################################
# 7. Accuracy
########################################################
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy: {:.2f}%".format(accuracy * 100))

########################################################
# 8. Confusion Matrix
########################################################
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

########################################################
# 9. Training vs Testing Accuracy
########################################################
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print("\nTraining Accuracy: {:.2f}%".format(train_acc * 100))
print("Testing Accuracy: {:.2f}%".format(test_acc * 100))

if train_acc > test_acc:
    print("Model may be overfitting.")
elif train_acc < test_acc:
    print("Model may be underfitting.")
else:
    print("Model is well balanced.")

########################################################
# 10. max_depth Comparison
########################################################
print("\nmax_depth Comparison:")
for depth in [1, 3, None]:
    temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    temp_model.fit(X_train, y_train)
    acc = temp_model.score(X_test, y_test)
    print("max_depth =", depth, " Test Accuracy = {:.2f}%".format(acc * 100))

########################################################
# 11. Feature Importances
########################################################
print("\nFeature Importances:")
importances = model.feature_importances_

for feature, importance in zip(X.columns, importances):
    print(feature, ":", round(importance, 3))

print("Most Important Feature:", X.columns[np.argmax(importances)])
print("Least Important Feature:", X.columns[np.argmin(importances)])

########################################################
# 12. Remove SleepHours
########################################################
X_no_sleep = data.drop(["SleepHours", "FinalResult"], axis=1)
y_no_sleep = data["FinalResult"]

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_no_sleep, y_no_sleep, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2, y_train2)

acc2 = model2.score(X_test2, y_test2)
print("\nAccuracy without SleepHours: {:.2f}%".format(acc2 * 100))

########################################################
# 13. Train Using Only StudyHours & Attendance
########################################################
X_small = data[["StudyHours", "Attendance"]]
y_small = data["FinalResult"]

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X_small, y_small, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_train3, y_train3)

acc3 = model3.score(X_test3, y_test3)
print("\nAccuracy using only 2 features: {:.2f}%".format(acc3 * 100))

########################################################
# 14. Predict for 5 New Students
########################################################
new_students = pd.DataFrame([
    [6, 85, 66, 7, 7],
    [3, 60, 50, 4, 6],
    [8, 92, 88, 9, 8],
    [4, 70, 55, 5, 6],
    [2, 50, 40, 2, 5]
], columns=X.columns)

predictions = model.predict(new_students)

print("\nPredictions for 5 Students:")
for i, pred in enumerate(predictions):
    result = "PASS" if pred == 1 else "FAIL"
    print("Student", i+1, ":", result)

########################################################
# 15. Manual Accuracy Calculation
########################################################
correct = 0
for actual, predicted in zip(y_test, y_pred):
    if actual == predicted:
        correct += 1

manual_acc = correct / len(y_test)
print("\nManual Accuracy: {:.2f}%".format(manual_acc * 100))

########################################################
# 16. Misclassified Students
########################################################
results = X_test.copy()
results["Actual"] = y_test.values
results["Predicted"] = y_pred

misclassified = results[results["Actual"] != results["Predicted"]]

print("\nMisclassified Students:")
print(misclassified)
print("Number of Misclassified Students:", len(misclassified))

########################################################
# 17. Random State Comparison
########################################################
print("\nRandom State Comparison:")
for state in [0, 10, 42]:
    temp_model = DecisionTreeClassifier(random_state=state)
    temp_model.fit(X_train, y_train)
    acc = temp_model.score(X_test, y_test)
    print("random_state =", state, " Accuracy = {:.2f}%".format(acc * 100))

########################################################
# 18. Decision Tree Visualization
########################################################
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns,
          class_names=["Fail", "Pass"], filled=True)
plt.show()

########################################################
# 19. Create New Column (PerformanceIndex)
########################################################
data["PerformanceIndex"] = (data["StudyHours"] * 2) + data["Attendance"]

X_new = data.drop("FinalResult", axis=1)
y_new = data["FinalResult"]

X_train4, X_test4, y_train4, y_test4 = train_test_split(
    X_new, y_new, test_size=0.2, random_state=42
)

model4 = DecisionTreeClassifier(random_state=42)
model4.fit(X_train4, y_train4)

acc4 = model4.score(X_test4, y_test4)
print("\nAccuracy with PerformanceIndex: {:.2f}%".format(acc4 * 100))

########################################################
# 20. max_depth=None Overfitting Check
########################################################
deep_model = DecisionTreeClassifier(max_depth=None, random_state=42)
deep_model.fit(X_train, y_train)

train_acc2 = deep_model.score(X_train, y_train)
test_acc2 = deep_model.score(X_test, y_test)

print("\nDeep Tree Training Accuracy: {:.2f}%".format(train_acc2 * 100))
print("Deep Tree Testing Accuracy: {:.2f}%".format(test_acc2 * 100))

print("\nProject Completed Successfully.")