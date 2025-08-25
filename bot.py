import tweepy 
import tkinter

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

user = api.get_user()
print(user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print('Followed everyone that is follow' + user.name)

root = Tk()
label1 = Label(root, text="Search")
E1 = Entry(root, bd = 5)
label2 = Label(root, text="Number Of Tweets")
E2 = Entry(root, bd = 5)
label3 = Label(root, text="Response")
E3 = Entry(root, bd = 5)
label4 = Label(root, text="Reply?")
E4 = Entry(root, bd = 5)
label5 = Label(root, text="Retweet?")
E5 = Entry(root, bd = 5)
label6 = Label(root, text="Favorite?")
E6 = Entry(root, bd = 5)
label7 = Label(root, text="Follow?")
E7 = Entry(root, bd = 5)





def mainFunction():
    search = "Keyword"
    numberOfTweets = "Number of tweets you wish to interact with"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.reweet()
            print("Retweeted the tweet")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    tweetId = tweet.user.idusername = tweet.user.screen_name
    phrase = "Very nice"
    for tweet in tweepy.Cursor(api.search,search).items(numberOfTweets):
        try:
            tweetId = tweet.user.id 
        except StopIteration:
            break
    getE1()
    search = getE1()
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = (int)(numberOfTweets)
    getE4()
    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            except StopIteration:
                break
    submit = Button(root, text ="Submit", command = mainFunction)

label1.pack()
E1.pack()
root.mainloop()

def getE1():
    return E1.get()
def getE2():
    return E2.get()
def get31():
    return E3.get()
def getE3():
    return E3.get()
def getE4():
    return E4.get()
def getE5():
    return E5.get()
def getE6():
    return E6.get()
def getE7():
    return E7.get()