class User():
    """9-3 The user class 9-5"""
    def __init__(self, first_name, last_name, login_attempts, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.user_info = user_info
        
    def describe_user(self):
        print("The user has following info: ")
        print("User's first_name is " + self.first_name)
        print("User's last_name is " + self.last_name)
        print("User's login_attempts is " + str(self.login_attempts))
        for key, value in self.user_info.items():
            print(key + ": " + value)

    def greet_user(self):
        print("I'm glad to meet you!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print("This instance login attempts is " + str(self.login_attempts))


pftom = User('wei', 'ge', 0, address='5005')
pfmRc = User('mrc', 'mrc', 0, address='4004')

pftom.describe_user()
pftom.greet_user()

print("\n")
pfmRc.describe_user()
pfmRc.greet_user()

pftom.increment_login_attempts()
pftom.print_login_attempts()

pftom.increment_login_attempts()
pftom.print_login_attempts()

pftom.increment_login_attempts()
pftom.print_login_attempts()

pftom.increment_login_attempts()
pftom.print_login_attempts()

pftom.reset_login_attempts()
pftom.print_login_attempts()


class Privileges():
    """
    A basic privilege class
    """

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("This person has following privileges: ")
        privileges = self.privileges
        for privilege in privileges:
            print("- " + privilege)


# 9-7 extend user for child class 
class Admin(User):
    """
    create a admin class for special handle
    """
    
    def __init__(self, first_name, last_name, login_attempts, privileges):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges(privileges)


uncle_tom = Admin('uncle', 'tom', 0, ['can add post', 'can delete', 'can ban user'])
uncle_tom.privileges.show_privileges()