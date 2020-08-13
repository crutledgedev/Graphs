import random
# from queue import Queue
from util import Queue, Stack
import time


class User:
    def __init__(self, name):
        self.name = name


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
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # !!!! IMPLEMENT ME

        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f"Collisions: {collisions}")

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
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid dups by ensuring first num < second num
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships
        random.shuffle(possible_friendships)

        # create friendships from the first N pairs of the list
        # N -> num_users * avg_friendships // 2
        N = num_users * avg_friendships // 2
        for i in range(N):
            friendship = possible_friendships[i]
            # user_id, friend_id = friendship
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                visited[v] = path

                for friend in self.friendships[v]:
                    path_copy = list(path)  # path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited

# import random
# from util import Queue, Stack


# class User:
#     def __init__(self, name):
#         self.name = name


# class SocialGraph:
#     def __init__(self):
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}

#     def add_friendship(self, user_id, friend_id):
#         """
#         Creates a bi-directional friendship
#         """
#         if user_id == friend_id:
#             print("WARNING: You cannot be friends with yourself")
#         elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
#             print("WARNING: Friendship already exists")
#         else:
#             self.friendships[user_id].add(friend_id)
#             self.friendships[friend_id].add(user_id)

#     def add_user(self, name):
#         """
#         Create a new user with a sequential integer ID
#         """
#         self.last_id += 1  # automatically increment the ID to assign the new user
#         self.users[self.last_id] = User(name)
#         self.friendships[self.last_id] = set()

#     def fy_shuffle(self, l):
#         for i in range(0, len(l)):
#             random_index = random.randint(i, len(l) - 1)
#             l[random_index], l[i] = l[i], l[random_index]

#     def populate_graph(self, num_users, avg_friendships):
#         """
#         Takes a number of users and an average number of friendships
#         as arguments

#         Creates that number of users and a randomly distributed friendships
#         between those users.

#         The number of users must be greater than the average number of friendships.
#         """
#         # Reset graph
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
#         # !!!! IMPLEMENT ME

#         # Add users
#         for user in range(num_users):
#             self.add_user(user)

#         # Create friendships

#         friendships = []
#         for user in range(1, self.last_id + 1):
#             for friend in range(user + 1, num_users + 1):
#                 friendship = (user, friend)
#                 friendships.append(friendship)

#         #
#         self.fy_shuffle(friendships)

#         # Take as many as we need
#         total_friendships = num_users * avg_friendships
#         random_friendships = friendships[:total_friendships//2]

#         # add to self.friendships
#         for friendship in random_friendships:
#             self.add_friendship(friendship[0], friendship[1])

#     def get_all_social_paths(self, user_id):
#         """
#         Takes a user's user_id as an argument

#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.
#         """
#         visited = {}  # Note that this is a dictionary, not a set
#         q = Queue()
#         q.enqueue([user_id])

#         while q.size():
#             path = q.dequeue()
#             current_user = path[-1]
#             if current_user not in visited:
#                 visited[current_user] = path
#                 friends = self.friendships[current_user]
#                 for friend in friends:
#                     new_path = path + [friend]
#                     q.enqueue(new_path)
#         return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
