
all_users = []

class User:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.name = name
        self.username = ""
        self.password = ""
        self.connections = ""

    def add_username(self, username):
        self.username = username

    def add_password(self, password):
        self.passwords = password

    def add_connections(self, connections):
        self.connections = connections

while True:

    inputtedname = input('Create an account. What is your name?')
    myuser = User(inputtedname)

    inputtedusername = input('Choose a username')
    myuser.add_username(inputtedusername)

    all_users.append(myuser)

    inputtedpassword = input('Choose a password')
    myuser.add_password(inputtedpassword)

    inputtedconnections = input('Choose a connection')
    myuser.add_connections(inputtedconnections)

    decision = input('Do you want to make another user? Type Y for yes and type N for no')

    if decision == 'N':
        break
