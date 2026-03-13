import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# load dataset
data = pd.read_csv("loan.csv")

# convert categorical data
data['Gender'] = data['Gender'].map({'Male':1,'Female':0})
data['Married'] = data['Married'].map({'Yes':1,'No':0})
data['Loan_Status'] = data['Loan_Status'].map({'Y':1,'N':0})

# split features and target
X = data.drop(columns='Loan_Status')
y = data['Loan_Status']

# split train test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# train model
model = LogisticRegression()
model.fit(X_train,y_train)

# save model
joblib.dump(model,"model.pkl")

print("Model trained and saved!")