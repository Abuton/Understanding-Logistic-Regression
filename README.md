## Understanding Logistic Regression Model
A simple logistic regression model to understand how it works the ins and out of it

A Logistic Regression Model is used to answer classification problem questions for instance
    1. How does the probability of getting lung cancer (yes or no) change for every additional pound a person is overweight and for every pack of cigarettes smoked per day?
    2. How much impact does a 0.1 increase in cavity or symmetry has on the probability of a diagnosed patient having a Benign kind of cancer?
    3. Does additional studyHour increases the probability of a student passing a course? if yes, by how much. if No by how much?
    
One thing that is common in these questions is yes or no (binary) pass or fail and probability. This gives intuition has to what Logistic Regression does when applied to a data for prediction or estimation.

Specifically Logistic Regression uses the log of odds as the dependent variable. It is estimated using Maximum Likelihood Estimation (MLE)
The simple math behind it functionality is called a logistic function AKA sigmoid function which takes any real number and map it into a value between 0 and 1. the sigmoid function gives an S shaped curve.

The question then arises: is logistic regression only for binary classification kind of problem?

Well the answer is No. There are other types of Logistic Regression
1. The Binary form is otherwise called Binomial Logistic Regression that is only 2 classes or 2 labels are possible 0 and 1 (yes or no)
2. The Multinomial Logistic Regression which deals with multiclass classification Problem. Multiclass is when we have 2 or more classes to predict examples include 
      * predict which color of jersey Barcelona would wear for their next match. So class could include (Pink, Blue, Green, yellow)
      * 
3. The Ordinal Logistic Regression: In this case the target variable has 3 or more Ordinal Categories. Ordinal in the sense that the classes are arranged in some form of hierachy examples include
      * Student grade (Excellent 5, Very Good 4, Good 3, Fair 2 and Poor 1)
      * Product ratings (1, 2, 3, 4, 5)
      
### Some Assumptions Binary Logistic Regression 
1. The target (dependent variable) should be dichotomous (binary) only 2 classes
2. There should be no Outliers in the data (scaled data is prefered)
3. There should be no high correlations (MultiCollinearity) among the predictors

Built a simple Logistic Regression to explain what it does and used some simple feature selection algorithm based on Feature Importance using the coef_ method. Which determines how important the features are in terms of predicting the classes using the predictors
Model has a 97% accuracy score and a 95% F1-score
