import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

# Step 1 : Load The DataSet

df = pd.read_csv("diabetes.csv")
print("\nFirst 5 Rows :\n",df.head())

# Step 2 : Data Preprocessing

# Replace 0 values with NaN
cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df[cols] = df[cols].replace(0,np.nan)


# Fill missing values with mean
df.fillna(df.mean(), inplace = True)

# Split Features And target
X = df.drop('Outcome', axis = 1)
Y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3 : Train Test Split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.2,random_state=42)

# Step 4 : Create Models
model_lr = LogisticRegression(max_iter=5000)
model_dt = DecisionTreeClassifier(random_state=42)
model_Knn = KNeighborsClassifier(n_neighbors=5)

# Train Models
model_lr.fit(X_train,Y_train)
model_dt.fit(X_train,Y_train)
model_Knn.fit(X_train,Y_train)

# Step 5 : Predictions

pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)
pred_Knn = model_Knn.predict(X_test)

# Step 6 : Evaluate The Models
def Evaluate(Y_test,Y_pred,name):
    acc = accuracy_score(Y_test,Y_pred)
    print(f"\n{name}")
    print("Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
    print("Classification Report:\n", classification_report(Y_test, Y_pred))
    return acc

acc_lr = Evaluate(Y_test,pred_lr, "Logistic Regression")
acc_dt = Evaluate(Y_test,pred_dt, "DecisionTree Classifier")
acc_Knn = Evaluate(Y_test,pred_Knn, "KNN")

# Step 7 : Compare Best Model
results = {
    "Logistic Regression" : acc_lr,
    "Decision Tree Classifier" : acc_dt,
    "KNN" : acc_Knn
}

best_model = max(results, key= results.get)

print("Best Model : ",best_model)
print("Best accuracy : ",results[best_model])

# Step 8 : Plot confusion Matrix
best_pred = {
    "Logistic Regression": pred_lr,
    "Decision Tree": pred_dt,
    "KNN": pred_Knn
}[best_model]

sns.heatmap(confusion_matrix(Y_test, best_pred), annot=True, fmt='d')
plt.title(f"Confusion Matrix - {best_model}")
plt.show()

# Step 9 : Save Predictions
Output = pd.DataFrame({
    'Actual' : Y_test,
    'Predicted' : pred_dt
})

Output.to_csv("diabetes_predictions.csv",index=False)
print("\nPredictions saved Successfully")