# Twitter-Email-Notification-API
This API allows you to track a specific keyword on Twitter and receive email notifications when it is tweeted

1- Installation:

* This API requires the following libraries to be installed: <code>tweepy</code> and <code>smtplib</code>.
* You can install them by running the following command in your command prompt: <code>pip install tweepy smtplib</code>


2- Twitter API Credentials:

* In order to use this API, you will need to have a Twitter developer account and create a new app to obtain your API credentials.
* Go to https://developer.twitter.com/en/apps and sign in with your Twitter account.
* Click on the <b>"Create an app"</b> button and fill out the required information.
* Once your app is created, navigate to the "Keys and Tokens" tab to obtain your Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
* Replace the placeholders for <b>consumer_key</b>, <b>consumer_secret</b>, <b>access_token</b>, <b>access_token_secret</b> in the code with your own credentials.


3- Email Credentials:

* You will also need to provide your email credentials in order to send the email notifications.
* Replace the placeholders for <b>email_address</b> and <b>email_password</b> in the code with your own email address and password.
* Note that this API uses the SMTP protocol to send emails, so you will need to have a SMTP server set up, or use an email service that supports SMTP, like Gmail.


4- Keyword to Track:

* You can set the keyword you want to track by replacing the placeholder for <b>keyword</b> in the code.
* The keyword is case-insensitive, it will be converted to lowercase before being checked against the tweet's text.


5- Running the API:

* Once you have set up your credentials and keyword, you can run the API by executing the code in your Python environment.
* The API will start streaming tweets and will send an email notification to your email address whenever a tweet containing the keyword is received.
* To stop the API, you can press CTRL + C in your command prompt.


6- Note:
* This API will only send notifications for tweets that are sent after the API was started, it will not notify for tweets that were sent before.
* It's also important to note that the API will be running indefinitely and will be listening to twitter stream and sending emails whenever it finds a match, So you should stop the API after your work is done.
* The API also uses your own email address to send email, so you should have an email configured with your email account and also should have less secure apps enabled for your email account.
* You can also change the email address to whom you want to send the email, by replacing the <b>email_address</b> in the server.sendmail() function.

7- Limitations:

* The Twitter API has certain limitations on the number of requests that can be made in a given time period. So, if you reach the limit of requests, the API will stop functioning until the limit resets.
* Additionally, the Twitter API only streams tweets from the past few days. So, tweets older than that will not be captured by this API.
* Also, you should be aware of your email usage limits and check with your email provider if there are any limitations on the number of emails that can be sent per day, or if there are any restrictions on sending emails through SMTP.


8- Error Handling:

* The API includes minimal error handling. If there are any errors encountered while connecting to the Twitter API or sending emails, they will be displayed in the command prompt.
* If you encounter any errors, you should check your credentials and network connection and try again.
* You can also check the twitter and email providers documentation for troubleshooting common issues.


9- Additional Resources

* For more information on using the Twitter API, check out the official documentation: https://developer.twitter.com/en/docs
* For more information on using the smtplib library, check out the official Python documentation: https://docs.python.org/3/library/smtplib.html
* For more information on using the tweepy library, check out the official documentation: http://docs.tweepy.org/en/latest/
