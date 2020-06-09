import random
from names import names, create_random_name

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

        # Create friendships
        total_friendships = round(avg_friendships * num_users)

        for i in range(total_friendships):

            user1ID = random.randrange(1, num_users + 1)
            user2ID = random.randrange(1, num_users + 1)
            
            # pick a different user ID for user2
            while user1ID == user2ID:
                user2ID = random.randrange(1, num_users + 1)

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
