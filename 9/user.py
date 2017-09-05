class User():
    """9-3 The user class"""
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        
    def describe_user(self):
        print("The user has following info: ")
        print("User's first_name is " + self.first_name)
        print("User's last_name is " + self.last_name)
        for key, value in self.user_info.items():
            print(key + ": " + value)

    def greet_user(self):
        print("I'm glad to meet you!")


pftom = User('wei', 'ge', address='5005')
pfmRc = User('mrc', 'mrc', address='4004')

pftom.describe_user()
pftom.greet_user()

print("\n")
pfmRc.describe_user()
pfmRc.greet_user()