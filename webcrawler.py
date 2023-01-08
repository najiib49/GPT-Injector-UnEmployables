# Reference: https://github.com/kesari007/Python-web-scraping-and-Sentiment-Analysis/blob/master/Source.py
import requests
from bs4 import BeautifulSoup  #web scraping library
from textblob import TextBlob   #importing textblob for sentiment analysis


def url_scrabber(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')  #parsing html pages

    review = soup.find_all("div")    # searching for the class and storing the content in variable review
    # review = soup.get_text()    # searching for the class and storing the content in variable review
    # print(review)
    # print(type(review))

    positive,negative,neutral=0,0,0
    x=0
    for i in review:
        text=i.get_text()
        x+=1
        sentiment=TextBlob(text).sentiment.polarity #sentiment lies in between -1 to 1
        if sentiment > 0:
            positive += 1
        elif sentiment ==0:
            neutral += 1
        elif sentiment < 0:
            negative += 1
    print("Positive reviews = ",positive)
    print("Neutral reviews = ",neutral)
    print("Negative reviews = ",negative)
    print("total reviews = ",x)

    return positive,negative,neutral, x

if __name__ == "__main__":
    url_scrabber("https://www.imdb.com/title/tt5956100/reviews")