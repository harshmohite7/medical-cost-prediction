import pandas as pd
import seaborn as sns 


insurance_data = pd.read_csv("data/insurance.csv")

sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"], hue=insurance_data["smoker"])
from sklearn.model_selection import train_test_split


X = insurance_data.drop(columns=["charges"])
y = insurance_data["charges"]
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#Train Model
from sklearn.linear_model import LinearRegression


model = LinearRegression()
model.fit(X_train,y_train)


y_pred = model.predict(X_test)


y_pred

y_test


from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print("R-squared:",r2)