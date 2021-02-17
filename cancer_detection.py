import streamlit as st
import pickle

st.markdown("""<style>
					body{
						background-color:lightgreen;
						color: #865690;
						}
				</style>""",
					 unsafe_allow_html=True)


st.title('A simple Health Application')

st.write("#### The App accepts some input features and produces an output that \
    says if a patient has benign or malignant kind of cancer")

right_column, left_column = st.beta_columns(2)

concavity_worst = right_column.number_input('concavity_worst')
symmentry = right_column.number_input('symmetry')
concavity_mean = right_column.number_input('concavity_mean')
concave_points_mean = right_column.number_input('concave_points_mean')
perimeter_worse = right_column.number_input('perimeter_worse')

compactness_worst = left_column.number_input('compactness_worst')
concave_points = left_column.number_input('concave_point')
compactness_mean = left_column.number_input('compactness_mean')
texture = left_column.number_input('texture')
area = left_column.number_input('area', step=10, min_value=20, max_value=300)

features_list = [concavity_worst, symmentry, concavity_mean, concave_points_mean, perimeter_worse, compactness_worst,
                concave_points,compactness_mean, texture, area]

model_name = "breast_cancer_ML_model.pkl"
model = pickle.load(open(model_name, 'rb'))

prediction = int(model.predict([features_list]))
prediction_proba = model.predict_proba([features_list])[:,0]
if prediction == 0: prediction='Benign'
else: prediction="Malignant"
diagnosis = st.button('Get Diagnosis')
if diagnosis:
    st.success(prediction)
    st.balloons()