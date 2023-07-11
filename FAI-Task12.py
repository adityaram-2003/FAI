#Bayesian Network
import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination


hd = pd.read_csv('heart.csv').replace('?', np.nan)
model = BayesianModel([
    *[('age', x) for x in ['trestbps', 'fbs']],
    *[(x, 'trestbps') for x in ['sex', 'exang']],
    *[(x, 'heartdisease') for x in ['trestbps', 'fbs']],
    *[('heartdisease', x) for x in ['chestecg', 'thalach', 'chol']]
])
model.fit(hd, estimator=MaximumLikelihoodEstimator)
infer = VariableElimination(model)
q1 = infer.query(variables=['heartdisease'], evidence={'chestecg': 1})
print(q1)
q2 = infer.query(variables=['heartdisease'], evidence={'cp': 1})
print(q2)