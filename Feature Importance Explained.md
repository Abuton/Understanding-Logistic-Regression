## Feature Importance 

Feature importance refers to techniques that assign a score to input features (predictors) based on how useful they are at predicting or estimating a target variable.
This means that, for each predictor that has been used to build a machine learning model, It has a part to play as to what the target will be.

There could a +ve value or -ve value assigned to each predictor. For a simple Logistic regression, the coef_ method of the algorithm is used to compute 
the feature importance of such feature. For other complex algorithm like Random Forest or Gradient Boosting algorithms, a method called feature_importance() is 
provided for any model built using the mentioned algorithms. NB the list of algorithm is not exhaustive, more could still be added.
Feature importance scores can be calculated for problems that involve predicting a numerical value, called regression, and those problems that involve 
predicting a class label, called classification.


### how important is Feature Importance to our Model?
Feature importance scores play an important role in a predictive modeling project, including providing insight into the data, insight into the model, and 
the basis for dimensionality reduction and feature selection that can improve the efficiency and effectiveness of a predictive model on the problem.
