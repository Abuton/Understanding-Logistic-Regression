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
    st.success(f"The patient is diagnosed with {prediction} cancer")





# SELECT max(speed) as maxspeed, min(speed) as minspeed,
# avg(speed) as avgspeed, highway
# FROM `qwiklabs-gcp-01-34dac731c423.demos.current_conditions`
# group by highway


# from google.cloud import storage, language_v1, bigquery

# # Set up our GCS, NL, and BigQuery clients
# storage_client = storage.Client()
# nl_client = language_v1.LanguageServiceClient()
# # TODO: replace YOUR_PROJECT with your project id below
# bq_client = bigquery.Client(project='qwiklabs-gcp-04-375802f9226d')

# dataset_ref = bq_client.dataset('news_classification_dataset')
# dataset = bigquery.Dataset(dataset_ref)
# table_ref = dataset.table('article_data') # Update this if you used a different table name
# table = bq_client.get_table(table_ref)

# # Send article text to the NL API's classifyText method
# def classify_text(article):
#         response = nl_client.classify_text(
#                 document=language_v1.types.Document(
#                         content=article,
#                         type_='PLAIN_TEXT'
#                 )
#         )
#         return response

# rows_for_bq = []
# files = storage_client.bucket('cloud-training-demos-text').list_blobs()
# print("Got article files from GCS, sending them to the NL API (this will take ~2 minutes)...")

# # Send files to the NL API and save the result to send to BigQuery
# for file in files:
#         if file.name.endswith('txt'):
#                 article_text = file.download_as_string()
#                 nl_response = classify_text(article_text)
#                 if len(nl_response.categories) > 0:
#                         rows_for_bq.append((str(article_text), str(nl_response.categories[0].name), str(nl_response.categories[0].confidence)))

# print("Writing NL API article data to BigQuery...")
# # Write article text + category data to BQ
# errors = bq_client.insert_rows(table, rows_for_bq)
# assert errors == []

# import pandas as pd

# percentiles = df['arrival_delay_deciles'].apply(pd.Series)
# percentiles.rename(columns = lambda x : '{0}%'.format(x*10), inplace=True)
# percentiles.head()