import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1 : Load The Dataset
fake_df = pd.read_csv("fake.csv")
true_df = pd.read_csv("true.csv")

# Add Label Column
fake_df["label"] = 0   
true_df["label"] = 1 
# Combine Datasets
df = pd.concat([fake_df, true_df], axis=0)

# Step 2 : Preprocessing
# Use Only text column
df = df[['text' , 'label']]

# Drop null Values
df.dropna(inplace=True)

# Convert to string
df['text'] = df['text'].astype(str)
#Feature and Target
X = df['text']
Y = df['label']

# Step 3 : Tf-Idf Vectorization
vectorizer = TfidfVectorizer(stop_words='english',max_df=0.7)
X_vect = vectorizer.fit_transform(X)

# Step 4 : Train Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X_vect,Y,test_size=0.2,random_state=42)

# Step 5 : Create Models
model_lr = LogisticRegression(max_iter=5000)
model_dt = DecisionTreeClassifier()

# Voting Classifier
voting_hard = VotingClassifier(estimators=[('lr',model_lr),('dt',model_dt)],voting= 'hard')

voting_soft = VotingClassifier(estimators=[('lr',model_lr),('dt',model_dt)],voting = 'soft')

# Step 6 : Train Models
model_lr.fit(X_train,Y_train)
model_dt.fit(X_train,Y_train)

voting_hard.fit(X_train,Y_train)
voting_soft.fit(X_train,Y_train)

# Step 7 : Predictions

pred_lr= model_lr.predict(X_test)
pred_dt=model_dt.predict(X_test)

pred_hard=voting_hard.predict(X_test)
pred_soft=voting_soft.predict(X_test)

# Step 8 : Evaluation
def evaluate(y_test, y_pred, name):
    print(f"\n{name}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

evaluate(Y_test,pred_lr,"Logistic Regression")
evaluate(Y_test,pred_dt,"Decision Tree")
evaluate(Y_test,pred_hard,"voting (Hard)")
evaluate(Y_test,pred_soft,"voting (soft)")

# Step 9 : Best Model
results = {
    "Logistic" : accuracy_score(Y_test,pred_lr),
    "Decision Tree" : accuracy_score(Y_test,pred_dt),
    "Voting Hard" : accuracy_score(Y_test,pred_hard),
    "Voting Soft" : accuracy_score(Y_test,pred_soft)
}

best_model = max(results , key=results.get)

print("Best Model : ",best_model)
print("Accuracy : ",results[best_model])