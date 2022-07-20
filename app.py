import streamlit as st
import pandas as pd
import numpy as np






st.markdown('# App Review Sentiment Detection')
st.write('The app will return the contradictory reviews where the sentiment of the review is positive but the star rating provided for it is not matching. The ***Run model*** buttonbutton shows result for given sample data and user can upload and run the model for custom data using ***upload and run***  also the user can download resulting data using the download button')

st.write('go to the [Github](https://github.com/prabinrajkp/streamlit_sentiment) to see more details')

st.markdown('---')

from preprocess import dataclean
from sentiment import setiment_analyze


col1,col2=st.columns(2)
with col1:
	run_b=st.button('Run model')
	
with col2:
	upload = st.file_uploader("Choose a csv file")
	b2=st.button('upload and run')
	
	
st.markdown('---')

st.markdown('### The contradictory reviews')

def convert_df(df):
   return df.to_csv().encode('utf-8')


if run_b==True:

	print('if cond')
	
	b=(7204, 10)
	ndf=pd.read_csv('ndf.csv')
	b2=ndf.shape
	col1, col2 = st.columns(2)
	col1.metric("The input data has", b[0], "rows")
	col2.metric("The model shows", b2[0], 'contradictory rows')
	
	st.dataframe(ndf)
	csv = convert_df(ndf)
	st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

elif upload is not None and b2==True:
	# Can be used wherever a "file-like" object is accepted:
	df = pd.read_csv(upload)	
	df=dataclean(df)
	ndf=setiment_analyze(df)
	b=df.shape
	b2=ndf.shape
	col1, col2 = st.columns(2)
	col1.metric("The input data has", b[0], "rows")
	col2.metric("The model shows", b2[0], 'contradictory rows')
	csv = convert_df(ndf)
	
	st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
	st.dataframe(ndf)
	#ndf






