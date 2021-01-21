# Password Manager - write a program that stores the user login info for a given website

class UserAccount:
    
    # ask for the domain username and password for the created object
    def __init__(self):
        self.file = open("PasswordManager.txt", "r")
        self.file_data = self.file.read()
        self.split_data = self.file_data.split("\n")
        self.file.close()
        
        self.domain = ''
        self.username = ''
        self.password = ''
        
# stores objects, websites, usernames, and passwords in a dictionary
def initialize_data(): # O(n)
    file = open("PasswordManager.txt", "r")
    file_data = file.read()
    split_data = file_data.split("\n")
    file.close()
               
    # initializing data objects
    
    objects = []
    for i in range(1, len(split_data), 4):
        temp = UserAccount()
        temp.domain = split_data[i].split()[1]
        temp.username = split_data[i+1].split()[1]
        temp.password = split_data[i+2].split()[1]
        objects.append(temp)
    return objects

# opens password manager txt file
def open_file(): # O(1)
    file = open("PasswordManager.txt", "a")
    file.close()

def domain_exists(data, domain): # O(n)
    for element in data:
        if element.domain == domain:
            return True
    return False
     
# adds a useraccount to a website
def add(): # O(n)
    data = initialize_data()
    temp = UserAccount()
    exists = domain_exists(data, temp.domain)
    cont = True
    while cont:
        temp.domain = input("Website: ")
        if exists:
            print("Website name already exists")
        else:
            temp.username = input("Username: ")
            temp.password = input("Password: ")
            file = open("PasswordManager.txt", "a")
            file.write("Account " + str(len(data)+1) + ':' + "\n")
            file.write("Website: " + str(temp.domain) + "\n")
            file.write("Username: " + str(temp.username) + "\n")
            file.write("Password: " + str(temp.password) + "\n")
            file.close()
            cont = False

# empties file
def empty(): # O(1) 
    file = open("PasswordManager.txt", "w")
    file.close()

def update_file(new_data): # O(n)
     empty()
     file = open("PasswordManager.txt", "a")
     for i in range(len(new_data)):
         file.write("Account " + str(i+1)+ ':' + "\n")
         file.write("Website: " + str(new_data[i].domain) + "\n")
         file.write("Username: " + str(new_data[i].username) + "\n")
         file.write("Password: " + str(new_data[i].password) + "\n")
     file.close()

def get_index(data, domain): # O(n)
    for i in range(len(data)):
        if data[i].domain == domain:
            return i

def remove(): # O(n)
    data = initialize_data()
    remove_website = input("Which website would you like to remove? ")
    exists = domain_exists(data, remove_website)
    if (len(data) < 1):
        print("No data to remove...")
    elif exists:
        index = get_index(data, remove_website)
        data.pop(index)     
        update_file(data)
    else:
        print("Domain error: 404 not found.")

def list_info(): # O(n)
    data = initialize_data()
    for i in range(len(data)):
         print("Account " + str(i+1))
         print("Website:  ", data[i].domain)
         print("Username: ", data[i].username)
         print("Password: ", data[i].password)

def change_password():
    data = initialize_data()
    website = input("For which website would you like to change the password? ")
    exists = domain_exists(data, website)
    if (len(data) < 1):
        print("No data to remove...")
    elif exists:
        index = get_index(data, website)
        data[index].password = input("Please enter new password: ")
        update_file(data)
    else:
        print("Domain error: 404 not found.")

# menu
def menu():
    print("Welcome to your own personal password manager!\nAll of your data will be stored by us in a discrete file on your desktop!")
    open_file()
    quit_program = False
    while quit_program == False:
        acnt_info = input("(A)dd account data, (R)emove prexisting account data, (C)hange Password, (E)mpty File, (L)ist Information,(Q)uit: ")
        if acnt_info == "A":
            add()                       
        
        elif acnt_info == "R":
            remove()

        elif acnt_info == "C":
            change_password()

        elif acnt_info == "E":
            empty()

        elif acnt_info == "L":
            list_info()

        elif acnt_info == "Q":
            quit_program = True

if __name__ == "__main__":
    menu()
