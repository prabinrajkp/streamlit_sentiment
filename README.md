# streamlit_sentiment

The sentiment analysis app makes use of transformers library from [Hugging face api](https://github.com/covid19india/api)

The app collects the review texts from the data and checks its sentiment and also see if 
there is an contrdiction between the the rating the user provided and the corresponding review.
That is, If a user gives a positive review for a particular app and he reted it 1/5 this can be considered as a contradiction so such rows are displayed 

By clicking on the **Run model** button the user can see the output generated for the default data 
The app also provides an option to **uplod coustom data** in the prefered format and **upload and run** button can be used to run the model on given data.

go to [Streamlit_sentiment](https://prabinrajkp-streamlit-sentiment-app-pcxqkk.streamlitapp.com/)

**NB: The model might take some time on running the custom data**

