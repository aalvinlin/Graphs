import random
from names import create_random_name

class User:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # impossible average: display an error message
        if avg_friendships >= num_users:
            print("Could not populate graph: The number of users must be greater than the average number of friendships.")
            return

        # Add users
        for i in range(1, num_users + 1):
            self.add_user(create_random_name())

        # Generate pairs of IDs to make friendships
        total_friendships = round(avg_friendships * num_users / 2)

        friendships_to_create = set()

        while len(friendships_to_create) < total_friendships:

            user1ID = random.randrange(1, num_users + 1)
            user2ID = random.randrange(1, num_users + 1)
            
            # pick a different user ID for user2
            while user1ID == user2ID:
                user2ID = random.randrange(1, num_users + 1)

            # ensure that the same two IDs are not added twice, such as (6, 4) and (4, 6)
            smallerID = user1ID if user1ID < user2ID else user2ID
            largerID = user1ID if user1ID > user2ID else user2ID

            friendships_to_create.add((smallerID, largerID))

        # create friendships
        for friendship in friendships_to_create:

            user1ID, user2ID = friendship
            self.add_friendship(user1ID, user2ID)
        
        print(f"\nSuccessfully populated graph with {num_users} users, each with an average of {avg_friendships} friendships.\n")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("users:\n  ", sg.users)
    print("friendships:\n  ", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("connections:\n  ", connections)

# 3. Questions

"""
1. To create 100 users with an average of 10 friends each, you would need to call add_frienship() 500 times.
The total number of links would be 100 * 10, but each call to add_frienship() makes 2 links at once. 1000 / 2 = 500.

2. If you create 1000 users with an average of 5 random friends each,

"""

# 4. Stretch
"""
1. No, results like the ones from question #2 above would not be realistic. To more closely model real-life distributions of friendships, the random generation of users should purposely include more people with very few or no friends (perhaps people who have just joined the network). Additionally, limits can be imposed on who can be friends with whom; people in the same geographic area may be more likely to form friendships, and there may be a higher average number of friendships in urban areas compared to rural areas. Another limit can be set on the total number of friends for any given user.
"""