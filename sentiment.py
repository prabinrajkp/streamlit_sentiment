from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def setiment_analyze(df):
	print("sentiment_started")
	polarity = [sentiment_pipeline(i) for i in df['senti_text']]
	print('model run')
	
	label=[]
	polarity_val=[]
	
	for i in polarity:
		label.append(list(i[0].values())[0])
		polarity_val.append(list(i[0].values())[1])
	df['sentiment_label']=label
	df['polarity_val']=polarity_val
	
	ndf=df[(df['Star']<=2) & (df['sentiment_label']=='POSITIVE') &  (df['polarity_val']>0.90)]
	ndf=ndf[['ID','User Name','Text','Star',]]
	ndf.reset_index(inplace=True)
	ndf.drop('index',axis=1,inplace=True)
	print('sentiment.py run')
	
	return ndf
    		
	
