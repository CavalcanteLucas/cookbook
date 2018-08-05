# Sorting Objects Without Native Comparison Support

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
users

sorted(users, key=lambda u: u.user_id)

from operator import attrgetter
sorted(users, key=attrgetter('user_id'))

#min(users, key=lambda u: u.user_id)
# TypeError: 'list' object is not callable