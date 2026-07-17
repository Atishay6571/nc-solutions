class Twitter:

    def __init__(self):
        #heap is required to sort 10 news from feeds of all users based on time
        self.time=0
        #hash maps for {user id: tweets}
        self.users={}
        #hash maps for {user id: following}
        self.following={}
        #hash maps for {user id: news feed}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.users:
            self.users[userId]=[[self.time,tweetId]]
        else:
            self.users[userId].append([self.time,tweetId])
        #just so that users can see own feeds too, at time of posting
        # we call follow to add user as following themselves.

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId,userId)
        followerList = self.following[userId]
        tweets=[]
        for user in followerList:
            if user in self.users:
                for tweet in self.users[user]:
                    tweets.append(tweet)
            else:
                continue
        
        heapq.heapify(tweets)
        while len(tweets)>10:
            heapq.heappop(tweets)
        tweets.sort()
        newsFeed=[tweet[1] for tweet in tweets]
        return newsFeed[::-1]



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=[followeeId]
        else:
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        else:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)  
        
