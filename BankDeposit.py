import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,roc_curve

# Step 1 : Load The Dataset

df = pd.read_csv("bank-full.csv",sep=';')

print("\nFirst 5 Recoreds :\n",df.head())

# Step 2 : Handle Missing / Unknown Values

# Replace Unkown with nan
df.replace("Unknown" , np.nan, inplace=True)

# Fill Missing values

df.ffill(inplace=True)

# Step 3 : Encode Categorical Data

#Convert Categorical columns using one hot encoding
df = pd.get_dummies(df,drop_first=True)

# Step 4 : Split Features And Target
X = df.drop('y_yes',axis=1)
Y = df['y_yes']

# Step 5 : Feature Scaling
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

# Step 5 : Train test split
X_train,X_test,Y_train,Y_test = train_test_split(X_Scaled,Y,test_size=0.2,random_state=42)

# Step 6 : Train models
model_lr = LogisticRegression(max_iter=5000)
model_Knn = KNeighborsClassifier(n_neighbors=5)
model_rf = RandomForestClassifier()

model_lr.fit(X_train,Y_train)
model_Knn.fit(X_train,Y_train)
model_rf.fit(X_train,Y_train)

# Step 7 : Predictions
pred_lr = model_lr.predict(X_test)
pred_Knn = model_Knn.predict(X_test)
pred_rf = model_rf.predict(X_test)

# Step 8 : Function Evaluation
def evaluate(y_test, y_pred, name):
    acc = accuracy_score(y_test, y_pred)
    print(f"\n{name}")
    print("Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return acc

acc_lr = evaluate(Y_test, pred_lr, "Logistic Regression")
acc_knn = evaluate(Y_test, pred_Knn, "KNN")
acc_rf = evaluate(Y_test, pred_rf, "Random Forest")


# Step 9 : Compare Models
results = {
    "Logistic Regression": acc_lr,
    "KNN": acc_knn,
    "Random Forest": acc_rf
}

best_model = max(results, key=results.get)
print("Best Model:", best_model)
print("Best Accuracy:", results[best_model])

# Step 10 : Plot Confusion Matrix
best_pred = {
    "Logistic Regression": pred_lr,
    "KNN": pred_Knn,
    "Random Forest": pred_rf
}[best_model]

sns.heatmap(confusion_matrix(Y_test, best_pred), annot=True, fmt='d')
plt.title(f"Confusion Matrix - {best_model}")
plt.show()

# Step 11 : ROC Curve
# Get probabilities
lr_prob = model_lr.predict_proba(X_test)[:,1]
knn_prob = model_Knn.predict_proba(X_test)[:,1]
rf_prob = model_rf.predict_proba(X_test)[:,1]

# ROC
fpr_lr, tpr_lr, _ = roc_curve(Y_test, lr_prob)
fpr_knn, tpr_knn, _ = roc_curve(Y_test, knn_prob)
fpr_rf, tpr_rf, _ = roc_curve(Y_test, rf_prob)

plt.plot(fpr_lr, tpr_lr, label="Logistic")
plt.plot(fpr_knn, tpr_knn, label="KNN")
plt.plot(fpr_rf, tpr_rf, label="Random Forest")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# Step 12 : Save OutPut

output = pd.DataFrame({
    'Actual': Y_test,
    'Predicted': best_pred
})

output.to_csv("bank_predictions.csv", index=False)

print("\nPredictions saved successfully!")


