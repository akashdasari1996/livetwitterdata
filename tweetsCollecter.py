import tweepy

SEP = ';'
csv = open('OutputStreaming.csv','a',encoding='utf-8')
csv.write('Date' + SEP + 'Text' + SEP + 'Location' + SEP + 'Number_Follower' + SEP + 'User_Name' + SEP + 'Friends_count\n')

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        Created = status.created_at.strftime("%Y-%m-%d-%H:%M:%S")
        Text = status.text.replace('\n', ' ').replace('\r', '').replace(SEP, ' ')
        Location = ''
        if status.coordinates is not None:
            lon = status.coordinates['coordinates'][0]
            lat = status.coordinates['coordinates'][1]
            Location = str(lat) + ',' + str(lon)       
        Follower = str(status.user.followers_count)
        Name = status.user.screen_name
        Friend = str(status.user.friends_count)
        csv.write(Created + SEP + Text + SEP + Location + SEP + Follower + SEP + Name + SEP + Friend + '\n')

    def on_error(self, status_code):
        print(status_code)

consumer_key = 'user_key'
consumer_secret = 'user_key'
access_token = 'user_key'
access_token_secret = 'user_key'

# stream
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
myStream = tweepy.Stream(auth, MyStreamListener())
myStream.filter(track=['#'])
