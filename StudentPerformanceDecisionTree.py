#########################################
# 1. Import required Libraries
#########################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

#########################################
# 2. Load The Dataset
#########################################

print("\n Load The Dataset")
data= pd.read_csv("student_performance_ml.csv")
print("Dataset Loaded Successfully")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

#########################################
# 3. Data Visualization
#########################################

plt.figure()
data["StudyHours"].hist()
plt.title("Study Hours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Count")
plt.show()

#########################################
# 4. Define Features (X) and Target (y)
#########################################

X = data.drop("FinalResult", axis=1)
y = data["FinalResult"]

#########################################
# 5. Train-Test Split
#########################################

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#########################################
# 6. Train Decision Tree Model
#########################################

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

#########################################
# 7. Predict on Test Data
#########################################

y_pred = model.predict(X_test)
print("\nActual vs Predicted:")
for actual, predicted in zip(y_test.values, y_pred):
    print("Actual:", actual, " Predicted:", predicted)

#########################################
# 8. Calculate Accuracy
#########################################

accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy: {:.2f}%".format(accuracy * 100))

#########################################
# 9. Confusion Matrix
#########################################

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

#########################################
# 10. Training vs Testing accuracy
#########################################

train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print("\nTraining Accuracy: {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy: {:.2f}%".format(test_accuracy * 100))

if train_accuracy > test_accuracy:
    print("Model may be overfitting.")
elif train_accuracy < test_accuracy:
    print("Model may be underfitting.")
else:
    print("Model is well balanced.")

#########################################
# 11. Compare Different max_depth values
#########################################

depths = [1, 3, None]

print("\nComparison of Different max_depth values:")
for depth in depths:
    temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    temp_model.fit(X_train, y_train)
    temp_pred = temp_model.predict(X_test)
    temp_accuracy = accuracy_score(y_test, temp_pred)
    print("max_depth =", depth, " Test Accuracy = {:.2f}%".format(temp_accuracy * 100))

#########################################
# 12. Predict for the new student
#########################################

new_student = pd.DataFrame([[6, 85, 66, 7, 7]],
                           columns=X.columns)

prediction = model.predict(new_student)

print("\nPrediction for New Student:")
if prediction[0] == 1:
    print("The student will PASS.")
else:
    print("The student will FAIL.")



print("\nProject Completed Successfully.")


