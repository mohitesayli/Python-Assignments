import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Get The data
    data = pd.read_csv("WinePredictor.csv")
    print("Dataset : ")
    print(data)

    X = data.drop("Class", axis=1)
    Y = data["Class"]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("\nActual vs Predicted class\n")

    for actual, predicted in zip(Y_test,Y_pred):
        print("Actaul : ", actual , "Predicted : ",predicted)

    print("\nAccuracy Of Model is : ",accuracy)

if __name__ == "__main__":
    main()