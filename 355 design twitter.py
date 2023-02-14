"""


Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

"""


class Twitter:

    def __init__(self):
        self.followers_dict = defaultdict(set)
        self.tweets_dict = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_dict[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        list_of_users = set(self.followers_dict[userId])
        list_of_users.add(userId)
        posts_heap = []

        for user in list_of_users:
            index = len(self.tweets_dict[user]) - 1
            if index >= 0:
                tweet_count, tweet_id = self.tweets_dict[user][index]
                heapq.heappush(posts_heap, [tweet_count, tweet_id, user, index - 1])

        total_count = 0
        tweet_ids = []
        while posts_heap and total_count < 10:
            tweet_count, tweet_id, user, index = heapq.heappop(posts_heap)
            tweet_ids.append(tweet_id)

            if index >= 0:
                tweet_count, tweet_id = self.tweets_dict[user][index]
                heapq.heappush(posts_heap, [tweet_count, tweet_id, user, index - 1])
            total_count += 1

        return tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_dict[followerId]:
            self.followers_dict[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)