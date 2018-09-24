package com.ispotabot;

import com.google.gson.Gson;
import twitter4j.Paging;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.api.TimelinesResources;
import twitter4j.conf.ConfigurationBuilder;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Date;
import java.util.List;

public class Main
{

	public static void main(String[] args)
	{
		TwitterResult twitterResult = new TwitterResult();
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).setOAuthConsumerKey("HSPtPoV8Hzmoqc2aYvFWvT3w5")
				.setOAuthConsumerSecret("dEbyUU5jtlePStchtfTh0uQyEGm93fKeXuqSx82F1rXisUw3eL")
				.setOAuthAccessToken("1022423423077806080-RmxkMyJvD3mwEJeD44W0JVp9dipz56")
				.setOAuthAccessTokenSecret("pDbA3pZ0CY76OV6HR2oHFqdNgPL7fVhGukxgHSbiXH498");
		TwitterFactory tf = new TwitterFactory(cb.build());
		Twitter twitter = tf.getInstance();

		TimelinesResources timelinesResources = twitter.timelines();

		int tweets_num = 0; // DONE
		double favorites_count = 0;// DONE
		double followers_count = 0;// DONE
		double friends_count = 0;// DONE
		double favorites_per_tweet = 0; // DONE
		long freqvency_minutes_per_tweet = 0; //DONE
		double hashtags_per_tweet = 0; // DONE
		Date oldDate = new Date(); // --
		Date newDate = new Date(); // --
		double max_hashtags = 0; // --
		double max_mentions = 0;
		double max_urls = 0;
		double mentions_per_tweet = 0;
		double urls_per_tweet = 0;
		double retweets_per_tweet = 0;
		double max_retweets = 0;
		long userId = 0;
		String name = "MarijaKilibarda";
		try
		{
			Paging paging = new Paging(1, 200);

			List<Status> statuses = twitter.getUserTimeline(name, paging);

			userId = statuses.get(0).getUser().getId();
			tweets_num = statuses.size();

			followers_count = statuses.get(0).getUser().getFollowersCount();
			friends_count = statuses.get(0).getUser().getFriendsCount();
			oldDate = statuses.get(0).getCreatedAt();
			newDate = statuses.get(0).getCreatedAt();
			for (Status status : statuses)
			{
				favorites_count += status.getFavoriteCount();
				max_hashtags += status.getHashtagEntities().length;
				max_mentions += status.getUserMentionEntities().length;
				max_urls += status.getURLEntities().length;
				max_retweets += status.getRetweetCount();

				if (status.getCreatedAt().after(newDate))
					newDate = status.getCreatedAt();

				if (status.getCreatedAt().before(oldDate))
					oldDate = status.getCreatedAt();
			}
			favorites_per_tweet = favorites_count/tweets_num ;
			hashtags_per_tweet = max_hashtags / tweets_num;
			retweets_per_tweet = max_retweets / tweets_num;
			freqvency_minutes_per_tweet = ((newDate.getTime() - oldDate.getTime())/1000/60)/tweets_num;

			System.out.println(freqvency_minutes_per_tweet);

		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
		}
		twitterResult.setTweets_num(tweets_num);
		twitterResult.setFavorites_count(favorites_count);
		twitterResult.setFollowers_count(followers_count);
		twitterResult.setFavorites_per_tweet(favorites_per_tweet);
		twitterResult.setFriends_count(friends_count);
		twitterResult.setFreqvency_minutes_per_tweet(freqvency_minutes_per_tweet);
		twitterResult.setHashtags_per_tweet(hashtags_per_tweet);
		twitterResult.setUserId(userId);
		twitterResult.setMentions_per_tweet(max_mentions/tweets_num);
		twitterResult.setHashtags_per_tweet(max_hashtags/tweets_num);
		twitterResult.setFriend_to_followers(friends_count/followers_count);
		twitterResult.setUrls_per_tweet(max_urls/tweets_num);
		twitterResult.setRetweets_per_tweet(retweets_per_tweet);
		String jsonResult = new Gson().toJson(twitterResult);

		try (PrintStream out = new PrintStream(new FileOutputStream(name + ".json"))) {
			out.print(jsonResult);
		}
		catch (FileNotFoundException e)
		{
			e.getMessage();
		}

	}

}
