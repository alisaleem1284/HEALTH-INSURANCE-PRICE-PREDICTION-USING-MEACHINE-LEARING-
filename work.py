
from sklearn.linear_model import LinearRegression 
x  = [[1],[2],[3],[4],[5]]
y = [40,50,65,75,90]
model = LinearRegression()
model.fit(x,y)
hours = float(input("hwo many houss to study = "))
predicate_marks = model.predict([[hours]])
print(f"base on the hours you study{hours} you may scored around{predicate_marks}")