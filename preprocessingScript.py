import numpy as np
import pandas as pd

dfs = []
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\fake_followers.csv\fake_followers.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_1.csv\social_spambots_1.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_2.csv\social_spambots_2.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_3.csv\social_spambots_3.csv\users.csv"))

dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\traditional_spambots_1.csv\traditional_spambots_1.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\traditional_spambots_2.csv\traditional_spambots_2.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\traditional_spambots_3.csv\traditional_spambots_3.csv\users.csv"))
dfs.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\traditional_spambots_4.csv\traditional_spambots_4.csv\users.csv"))
botsCsv = pd.concat(dfs, sort=True)
botsCsv['is_bot'] = 1

print("Fake users done!")
dfs = []
dfs.append(pd.read_csv(r'C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\genuine_accounts.csv\genuine_accounts.csv\users.csv'))

print("Human users done!")

humansCsv = pd.concat(dfs, sort=True)
humansCsv['is_bot']=0

resultUsers = pd.concat([botsCsv, humansCsv], sort=True)

users = pd.DataFrame()
users['id']=resultUsers['id']
users['friends_count'] = resultUsers['friends_count']
users['favorites_count'] = resultUsers['favourites_count']
users['followers_count'] = resultUsers['followers_count']
users['friends_to_followers_ratio'] = resultUsers['friends_count']/resultUsers['followers_count']
users['is_bot'] = resultUsers['is_bot']

del dfs
del botsCsv
del humansCsv

dfs2 = []
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\fake_followers.csv\fake_followers.csv\tweets.csv"))
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_1.csv\social_spambots_1.csv\tweets.csv"))
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_2.csv\social_spambots_2.csv\tweets.csv"))
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\social_spambots_3.csv\social_spambots_3.csv\tweets.csv"))
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\traditional_spambots_1.csv\traditional_spambots_1.csv\tweets.csv"))
dfs2.append(pd.read_csv(r"C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\genuine_accounts.csv\genuine_accounts.csv\tweets.csv"))

print("Fake tweeters done!")

botsTweets = pd.concat(dfs2, sort=True)

del dfs2
dfs2 = []
dfs2.append(pd.read_csv(r'C:\Users\Nemanja.Antic\Downloads\cresci2017\cresci-2017.csv\datasets_full.csv\fake_followers.csv\fake_followers.csv/tweets.csv'))
humansTweets = pd.concat(dfs2, sort=True)

print("Human tweeters done!")

resultTweets = pd.concat([botsTweets, humansTweets], sort=True)
del botsTweets
del humansTweets

def get_mentions_per_tweet(userId,tweets):
    result = {}
    userTweets = tweets.query('user_id ==' + str(userId))
    result['num_mentions'] = sum(userTweets['num_mentions'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['num_hashtags'] = sum(userTweets['num_hashtags'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['num_urls'] = sum(userTweets['num_urls'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['retweet_count'] = sum(userTweets['retweet_count'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    result['favorite_count'] = sum(userTweets['favorite_count'])/userTweets.shape[0] if userTweets.shape[0] > 0 else 0
    return result

men_per_tweet_list =[]
urls_per_tweet_list =[]
hashtags_per_tweet_list =[]
retweets_per_tweet_list =[]
favs_per_tweet_list =[]

for user in users['id']:
    result = []
    result = get_mentions_per_tweet(user,resultTweets)
    men_per_tweet_list.append(result['num_mentions'])
    hashtags_per_tweet_list.append(result['num_hashtags'])
    urls_per_tweet_list.append(result['num_urls'])
    retweets_per_tweet_list.append(result['retweet_count'])
    favs_per_tweet_list.append(result['favorite_count'])
    print(user)


users['mentions_per_tweet'] = np.array(men_per_tweet_list)
users['hashtags_per_tweet'] = np.array(hashtags_per_tweet_list)
users['urls_per_tweet'] = np.array(urls_per_tweet_list)
users['retweets_per_tweet'] = np.array(retweets_per_tweet_list)
users['favorites_per_tweet'] = np.array(favs_per_tweet_list)

writer = pd.ExcelWriter('cresci2017Preprocessed.xlsx', engine='xlsxwriter')
users.to_excel(writer, sheet_name='Sheet1')
writer.save()

users.to_csv('cresci2017Preprocessed.csv')