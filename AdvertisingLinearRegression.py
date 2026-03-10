import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Get The data
data = pd.read_csv("Advertising.csv")
data = data.drop("Unnamed: 0", axis=1)
print("Dataset : ")
print(data)

# Clean,Prepare and Manipulate The Data
X = data[['TV','radio', 'newspaper']]
Y = data["sales"]

# Train The data
X_train, X_test, Y_train, Y_Test = train_test_split(X,Y,test_size=0.5)

Model = LinearRegression()
Model.fit(X_train,Y_train)

# Test The data
Y_pred = Model.predict(X_test)

# Display Expected vs Predicted Values
print("\nExpected vs Predicted sales\n")

for actual,predicted in zip(Y_Test,Y_pred):
    print("Actual : ",actual, "Predicted : ",round(predicted,2))