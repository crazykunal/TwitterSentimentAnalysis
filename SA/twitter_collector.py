import tweepy
from tweepy.auth import OAuthHandler
from textblob import TextBlob
# import json
# import plotly
# import plotly.express as px

#Graph defining section
# fig = go.Figure()
# colors = ['lightslategray',] * 5
# colors[2] = 'crimson'

#Configuration section
def twitter():
    consumer_key = 'A8WigDC2yBaHDqcf1xKuUiMci'
    consumer_key_secret = 'd4VnAAz9XXauQl6XGYg9QuMF3uT0TX3UkAS2q8coPvxDfznec3'
    access_token = '1355180761352122370-nOI1IwSsBLWme7QVquhYemzRXAXLdn'
    access_token_secret = 'ceDgmFe44m5Nc6jX9zbrR7toWKAp8mafywRZMCKFyDP0m'

    #Fetching tweets from twitter that matches search criterion - UIIC
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.search('UIIC')

    #Defining counters
    VeryPositive, Positive, Neutral, Negative, VeryNegative = 0, 0, 0, 0, 0

    #Quantifying tweets according to their sentiment
    for tweet in public_tweets:
        #print(tweet.text)
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        if 0.5 <= analysis.sentiment[0] < 1:
            VeryPositive += 1

        elif 0.1 <= analysis.sentiment[0] <= 0.5:
            Positive += 1

        elif -0.1 <= analysis.sentiment[0] < 0.1:
            Neutral += 1

        elif -0.5 <= analysis.sentiment[0] < -0.1:
            Negative += 1

        else:
            VeryNegative += 1

    #list declaration
    x = ['VeryPositive', 'Positive', 'Neutral', 'Negative', 'VeryNegative']
    y = [VeryPositive, Positive, Neutral, Negative, VeryNegative]
    print("Very Positive", VeryPositive)
    print("Positive", Positive)
    print("Neutral", Neutral)
    print("Negative", Negative)
    print("VeryNegative", VeryNegative)
    return y
# def twitter():
#     #Plotting the graph
#     fig = px.bar(x=x, y=y, color=colors, title="Twitter Sentiment Analysis")
#     #Decorating the graph

#     graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEnconder)
#     #Show the graph
#     return graph

#print the result
# print("Very Positive", VeryPositive)
# print("Positive", Positive)
# print("Neutral", Neutral)
# print("Negative", Negative)
# print("VeryNegative", VeryNegative)