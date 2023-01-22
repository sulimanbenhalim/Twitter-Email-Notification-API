import tweepy
import smtplib

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Email credentials
email_address = "YOUR_EMAIL_ADDRESS"
email_password = "YOUR_EMAIL_PASSWORD"

# Keyword to track
keyword = "example"

# Connect to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if keyword in status.text.lower():
            # Send email notification
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_address, email_password)
            subject = "Keyword '" + keyword + "' was tweeted"
            body = status.text
            message = 'Subject: {}\n\n{}'.format(subject, body)
            server.sendmail(email_address, email_address, message)
            server.quit()

# Start streaming tweets
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=[keyword])
