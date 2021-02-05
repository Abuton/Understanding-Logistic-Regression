from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_name = 'pickled_files/breast_cancer_ML_model.pkl'
model = pickle.load(open(model_name, 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	"""For predicting diagnosis result
	"""

	features = [int(x) for x in request.form.values()]
	final_features = [np.array(features)]
	prediction = model.predict(final_features)


	return render_template('index.html', prediction_text=f'Result of the diagnosis test is {prediction[0]}')

if __name__ == '__main__':
	app.run(debug=True, port=80)