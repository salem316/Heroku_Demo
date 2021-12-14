import pandas as pd

datos=pd.read_excel("dataset.xlsx")

X=datos[["Experience","Test-score","Interview_score"]]

y=datos["Salary"]

# print(X)
# print("="*60)
# print(y)

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()

regressor.fit(X,y)

# print(regressor.predict([[0,8,9]]))

import pickle

pickle.dump(regressor,open("model.pkl","wb"))

model=pickle.load(open("model.pkl","rb"))

print(model.predict ([[2,9,6]]))


