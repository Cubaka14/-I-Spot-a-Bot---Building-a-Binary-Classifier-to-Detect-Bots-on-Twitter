package com.ispotabot;

public class TwitterResult
{
	private long userId;
	private int tweets_num;
	private double favorites_count;
	private double followers_count;
	private double friends_count;
	private double favorites_per_tweet;
	private long freqvency_minutes_per_tweet;
	private double hashtags_per_tweet;
	private double mentions_per_tweet;
	private double urls_per_tweet ;
	private double friend_to_followers;
	private double retweets_per_tweet;

	public double getRetweets_per_tweet(){ return retweets_per_tweet;}
	public void setRetweets_per_tweet(double retweets_per_tweet){this.retweets_per_tweet = retweets_per_tweet;}
	public double getFriend_to_followers()
	{
		return friend_to_followers;
	}

	public void setFriend_to_followers(double friend_to_followers)
	{
		this.friend_to_followers = friend_to_followers;
	}

	public int getTweets_num()
	{
		return tweets_num;
	}

	public void setTweets_num(int tweets_num)
	{
		this.tweets_num = tweets_num;
	}

	public double getMentions_per_tweet()
	{
		return mentions_per_tweet;
	}

	public void setMentions_per_tweet(double mentions_per_tweet)
	{
		this.mentions_per_tweet = mentions_per_tweet;
	}

	public double getUrls_per_tweet()
	{
		return urls_per_tweet;
	}

	public void setUrls_per_tweet(double urls_per_tweet)
	{
		this.urls_per_tweet = urls_per_tweet;
	}

	public double getFavorites_count()
	{
		return favorites_count;

	}

	public long getUserId()
	{
		return userId;
	}

	public void setUserId(long userId)
	{
		this.userId = userId;
	}

	public void setFavorites_count(double favorites_count)
	{
		this.favorites_count = favorites_count;
	}

	public double getFollowers_count()
	{
		return followers_count;
	}

	public void setFollowers_count(double followers_count)
	{
		this.followers_count = followers_count;
	}

	public double getFriends_count()
	{
		return friends_count;
	}

	public void setFriends_count(double friends_count)
	{
		this.friends_count = friends_count;
	}

	public double getFavorites_per_tweet()
	{
		return favorites_per_tweet;
	}

	public void setFavorites_per_tweet(double favorites_per_tweet)
	{
		this.favorites_per_tweet = favorites_per_tweet;
	}

	public long getFreqvency_minutes_per_tweet()
	{
		return freqvency_minutes_per_tweet;
	}

	public void setFreqvency_minutes_per_tweet(long freqvency_minutes_per_tweet)
	{
		this.freqvency_minutes_per_tweet = freqvency_minutes_per_tweet;
	}

	public double getHashtags_per_tweet()
	{
		return hashtags_per_tweet;
	}

	public void setHashtags_per_tweet(double hashtags_per_tweet)
	{
		this.hashtags_per_tweet = hashtags_per_tweet;
	}
}
