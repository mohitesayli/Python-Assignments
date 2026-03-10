import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("PlayPredictor.csv")
data = data.drop("Unnamed: 0", axis=1)

print("Dataset:")
print(data)

# Step 2 : Clean, Prepare and Manipulate Data

le = LabelEncoder()

data["Weather"] = le.fit_transform(data["Weather"])
data["Temperature"] = le.fit_transform(data["Temperature"])
data["Play"] = le.fit_transform(data["Play"])

print("\nEncoded Dataset:")
print(data)

# Features and Target
X = data[["Weather", "Temperature"]]
y = data["Play"]

# Step 3 : Train Model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

# Step 4 : Test Data

y_pred = knn.predict(X_test)

print("\nActual vs Predicted:")
for a, p in zip(y_test.values, y_pred):
        print("Actual:", a, " Predicted:", p)

# Example Prediction
print("\nPrediction for Weather=Sunny Temperature=Cool")

sample = pd.DataFrame([[2,0]], columns=["Weather","Temperature"])

result = knn.predict(sample)

if result == 1:
    print("Play = Yes")
else:
    print("Play = No")
# Step 5 : Calculate Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy of Model:", accuracy)
