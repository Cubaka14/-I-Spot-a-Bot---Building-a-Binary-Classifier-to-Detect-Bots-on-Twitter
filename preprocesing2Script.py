import numpy as np
import pandas as pd

list_humans_pandas = []
list_humans_pandas.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\E13\users.csv"))
list_humans_pandas.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\TFP\users.csv"))
humans = pd.concat(list_humans_pandas)
humans['is_bot'] = 0

list_bot_pandas = []
list_bot_pandas.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\INT\users.csv"))
list_bot_pandas.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\FSF\users.csv"))
list_bot_pandas.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\TWT\users.csv"))
bots = pd.concat(list_bot_pandas, sort=True)
bots['is_bot'] = 1

cresci2015_users = pd.concat([humans,bots],sort = True)
cresci2015_users['friends_to_followers_ratio'] = cresci2015_users['friends_count']/cresci2015_users['followers_count']

users = pd.DataFrame()
users['id']=cresci2015_users['id']
users['friends_to_followers_ratio'] = cresci2015_users['friends_to_followers_ratio']
users['friends_count'] = cresci2015_users['friends_count']
users['favorites_count'] = cresci2015_users['favourites_count']
users['followers_count'] = cresci2015_users['followers_count']
users['is_bot'] = cresci2015_users['is_bot']

list_humans_pandas_2 = []
list_humans_pandas_2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\E13\tweets.csv"))
list_humans_pandas_2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\TFP\tweets.csv"))
humans_2 = pd.concat(list_humans_pandas_2, sort = True)

list_bot_pandas_2 = []
list_bot_pandas_2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\FSF\tweets.csv"))
list_bot_pandas_2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\INT\tweets.csv"))
list_bot_pandas_2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Desktop\iSpotABot\cresci-2015\TWT\tweets.csv"))
bots_2 = pd.concat(list_bot_pandas_2)
cresci2015_tweets = pd.concat([humans_2,bots_2])

def getFrequencyTweets(listOfDates):
    x = pd.to_datetime(listOfDates).agg(['min','max'])
    print(x.max())
    print(x.min())
    print(x.max()-x.min())
    return (x.max() - x.min())/listOfDates.shape[0]

def get_tweet_stats(userId,tweets):
    result={}
    userTweets = tweets.query('user_id ==' + str(userId))
    result['num_mentions'] = sum(userTweets['num_mentions'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['num_urls'] = sum(userTweets['num_urls'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['num_hashtags'] = sum(userTweets['num_hashtags'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['retweet_count'] = sum(userTweets['retweet_count'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['favorite_count'] = sum(userTweets['favorite_count'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['frequ_minutes_tweet'] = getFrequencyTweets(userTweets['timestamp']).total_seconds()/60
    return result


men_per_tweet_list = []
urls_per_tweet_list = []
hashtags_per_tweet_list = []
retweets_per_tweet_list = []
favorite_per_tweet_list = []
frequ_minutes_tweet_list = []

type(cresci2015_tweets['timestamp'].values[0])
type(pd.to_datetime(cresci2015_tweets['timestamp']))
test = pd.to_datetime(cresci2015_tweets['timestamp'])

for item in cresci2015_users['id']:
    tweets_stat_map = get_tweet_stats(item,cresci2015_tweets)
    men_per_tweet_list.append(tweets_stat_map['num_mentions'])
    urls_per_tweet_list.append(tweets_stat_map['num_urls'])
    hashtags_per_tweet_list.append(tweets_stat_map['num_hashtags'])
    retweets_per_tweet_list.append(tweets_stat_map['retweet_count'])
    favorite_per_tweet_list.append(tweets_stat_map['favorite_count'])
    frequ_minutes_tweet_list.append(tweets_stat_map['frequ_minutes_tweet'])

users['men_per_tweets'] = np.array(men_per_tweet_list)
users['urls_per_tweets'] = np.array(urls_per_tweet_list)
users['hashtags_per_tweets'] = np.array(hashtags_per_tweet_list)
users['retweets_per_tweets'] = np.array(retweets_per_tweet_list)
users['favorite_per_tweets'] = np.array(favorite_per_tweet_list)
users['frequ_minutes_tweet'] = np.array(frequ_minutes_tweet_list)

writer = pd.ExcelWriter('cresci2015Prepocessed.xlsx', engine='xlsxwriter')
users.to_excel(writer, sheet_name='Sheet1')
writer.save()

users.to_csv('cresci2015Preprocessed.csv')
