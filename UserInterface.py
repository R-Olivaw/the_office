"""

This module contains the user interface.

"""

class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    

if __name__ == "__main__":

    import sys
    # the variable we'll use for the user's name.
    user_name = None
    # continue to ask for the user's name until a valid response is given.
    while not user_name: 
        print("Welcome to Dunder Miflin Scranton Branch!\nWhat's your name?")
        # ensure the user's input is in a valid form (e.g. Billy Joel)
        user_name = input("Name: ").title()
        
        # shame the user for having a long name.
        if len(user_name) > 100:
            print(user_name[:5]+"...whatnow?")
        
        # make sure the user has input an actual name.
        else:
            import re
            nameRegex = re.compile(r'^[a-zA-Z ]+$') 
            
            # Separate the user's name into first and last.
            if nameRegex.search(user_name):
                firstNameRegex = re.compile(r'[a-zA-Z]+')
                mo = firstNameRegex.search(user_name)
                user_first_name = mo.group()
                user_last_name = user_name[len(user_first_name)+1:]
                
                if user_first_name in ["Toby"]:
                    print("NOOOO! NOOOOO! GOD! NO!")
                    sys.exit("TOBY DETECTED")
    
            # Shame the user for giving us a fake name.
            else:
                print("Not a name!")
    
    # create the user object
    user = User(user_first_name, user_last_name)
    # program off switch    
    user_quit_decision = False
    
    
    # welcome message
    print("Welcome to Dunder Miflin Scranton Branch, " + user_first_name + "!")
    
    # begin program loop
    while not user_quit_decision:
        print("where do you want to go?")
        user_quit_decision = True