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

Feature Importance can be used to improve the performance of a predictive model: this can be achived by selecting only the most importanct features from the list of prectors
and training your model with those features. 

Feature Importance helps to reduce model complexity: What this means is that instead of training a ML model with 30 features, computing feature importance can afford you the chance to build the model with just 10 models and still have a good score in terms of evaluation. It possible you get even a better score

### Some of the disadvantage of Feature Importance
1. Sometimes removing less important features reduce the performance of the model

