
import joblib
# from sklearn.externals import joblib
ml = joblib.load('MLmodel')
p=ml.predict([[33]])
print(p)
print("hello")