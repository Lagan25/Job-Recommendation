import pandas as pd 


def clean_data(job_df):
	print(job_df.head(20))





job_df = pd.read_csv('data.csv')
clean_data(job_df)