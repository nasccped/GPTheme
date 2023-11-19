"""
Here we can see a Python code containing some (not all) of the language's features. This one may be a little more worked than the others. Python was the first programming language I learned, and you can run the code too. It's very interactive :^)
"""

# Importing a useful library
from typing import Union

# Terminal color printer dictionary
colors_dict = {
    "Black" : "\033[1;30m",
    "Red" : "\033[1;31m",
    "Green" : "\033[1;32m",
    "Yellow" : "\033[1;33m",
    "Blue" : "\033[1;34m",
    "Magenta" : "\033[1;35m",
    "Cyan" : "\033[1;36m",
    "White" : "\033[1;37m",
    "Reset" : "\033[0m"
}

# Similar to the one above, but for specific cases
styles_dict = {
    "Non Object User Indicator" : f"\033[3;37m? {colors_dict['Reset']}",
    "Out Scope Response" : "\033[4;31m",
    "Me suggestions" : "\033[4;30m",
    "User Response" : "\033[4;38;0m"
}

# User attributes that will be useful later
user_dict = {
    "Name" : None,
    "Age" : None,
    "Color Name" : None,
    "Color Itself" : None,
    "Nationality" : None,
}

# Creating a class
class Person:

    """
    An object called Person, for obvious reasons...
    """

    # Creating the object Person
    def __init__(self, name:str, age:Union[int, str], color_name:str, color_itself:str, nationality:str) -> None:
        
        # If age parameter type == string 
        if isinstance(age, str):

            # Importing some libraries
            from datetime import datetime

            # Setting the age by current date
            current_date = datetime.now()
            born_date = age.split("-")
            born_date = datetime(int(born_date[0]), int(born_date[1]), int(born_date[2]))
            age = current_date.year - born_date.year

            # deleting the (NOW) useless things
            del datetime, born_date, current_date
        ### Else, do nothing

        # Important object attributes
        self.name = name
        self.age = age
        self.color_name = color_name
        self.color_itself = color_itself
        self.nationality = nationality

        # Not so important things
        self.phrase_indicator = self.color_itself + "> " + colors_dict['Reset']

        # deleting the (NOW) useless variables
        del name, age, color_name, color_itself, nationality
    ###

    # Self explanatory
    def terminalClear(self) -> None:

        # Importing some libraries
        import os, platform
        
        # if your OS == .
        if platform.system() == "Windows":

            # do this
            os.system('cls')
        
        # else
        else:

            # do that
            os.system('clear')

        # deleting the (NOW) useless libraries
        del os, platform
    ###

    # In situations like when I ask for a number and you give me a sentence XD
    def outScopeResponse(self, message:str, wait_response:bool = True) -> None:

        # Importing some libraries
        import getpass

        # Printing the message
        print(f"{styles_dict['Out Scope Response']}{message}{colors_dict['Reset']}", end = "")

        if wait_response:
        
            # waiting for interaction
            interaction = getpass.getpass("")
        ###

        else:

            interaction = None

            # To break line
            print()
        ###

        # deleting the (NOW) useless libraries / variables
        del getpass, interaction
    ###

    # Declaring who is speaking based on the arrow and its color
    def personSpeak(self, phrase:str, end:str = "\n") -> None:

        # Simple printer
        print(f"{self.phrase_indicator}{phrase}", end = end)
    ###

    # Personal suggestion
    def personSuggestion(self, suggestion:str, personal_end:str = "\n") -> None:

        # Printing the suggestion
        print(f"{self.color_itself}{suggestion}{colors_dict['Reset']}", end = personal_end)
    ###

    # Setting an auto conversation between you and me!
    def autoConversation(self, step:int) -> None:

        # If conversation starts:
        if step == 0:

            # Cleaning terminal
            self.terminalClear()

            # Asking your name
            self.personSpeak("Hi there! What's your name?")

            # Storing your name
            user_dict["Name"] = input(f"{styles_dict['Non Object User Indicator']}{styles_dict['User Response']}")

            # To reset font / break 1 line
            print(f"{colors_dict['Reset']}")
        ###
        
        # If it's 2º step conversation
        elif step == 1:

            # Cleaning terminal
            self.terminalClear()
            
            # Printing saudation
            self.personSpeak(f"Hi {user_dict['Name']}! I'm {self.name}, also my favorite color is {self.color_itself}{self.color_name}!{colors_dict['Reset']} What is yours?")

            # creating a list with color names and values to show in `for loop`
            color_names = list(colors_dict.keys())
            color_selfs = list(colors_dict.values())

            # For loop to show the colors table >>> i range = range by row / j range = range by column
            for i in range(2):

                for j in range(4):

                    # Setting the specific color name and value from the list
                    print(f"{(i * 4) + j + 1}. {color_selfs[(i * 4) + j]}{color_names[(i * 4) + j]}?{colors_dict['Reset']}", end=(" " * (10 - len(color_names[(i * 4) + j]))))
                ###

                # Breaking the line by the row
                print()
            ###

            # Breaking the line by no reason
            print()
            
            # Giving a suggestion
            self.personSuggestion("> You can chose by number:", "")

            # Storing the selected color
            color = input(f"{styles_dict['Non Object User Indicator']}{styles_dict['User Response']}")

            # To reset font / break 1 line
            print(f"{colors_dict['Reset']}")

            # if you have answered as you should
            if color.isdigit():

                # Turning variable into int
                color = int(color)

                # If the answer is within scope
                if color > 0 and color < 9:

                    # Turning response value into the list index
                    color -= 1

                    # Catching color data by new value
                    user_dict["Color Name"] = color_names[color]
                    user_dict["Color Itself"] = color_selfs[color]
                ###
                    
                # If the answer is out of scope
                else:

                    # Show error message
                    self.outScopeResponse(f"Sorry, I couldn't understand your answer :^( \nBut for now, let's consider that you answered:{colors_dict['Reset']}{colors_dict['White']}'White'!{colors_dict['Reset']}")

                    # Putting acceptable values into user dictionary
                    user_dict["Color Name"] = "White"
                    user_dict["Color Itself"] = colors_dict["White"]
                ###

            # Else
            else:

                # Show error message
                self.outScopeResponse(f"Sorry, I couldn't understand your answer :^( \nBut for now, let's consider that you answered:{colors_dict['Reset']}{colors_dict['White']}'White'!{colors_dict['Reset']}")

                # Putting acceptable values into user dictionary
                user_dict["Color Name"] = "White"
                user_dict["Color Itself"] = colors_dict["White"]
            ###

            # deleting the (NOW) useless libraries / variables
            del color, color_names, color_selfs
        ###

        # If it's 3º step conversation
        elif step == 2:

            # Cleaning terminal
            self.terminalClear()
            
            # Asking your nationality
            self.personSpeak("I would also like to know where you are from...")

            # Storing your nationality
            user_dict["Nationality"] = input(f" {styles_dict['Non Object User Indicator']}{styles_dict['User Response']}")

            # To reset font / break 1 line
            print(f"{colors_dict['Reset']}")
        ###
        
        # If it's 4º step conversation
        elif step == 3:

            # Cleaning terminal
            self.terminalClear()

            # Asking your age
            self.personSpeak("And lastly, how old are you?")

            # Storing your age
            age = input(f"{styles_dict['Non Object User Indicator']}{styles_dict['User Response']}")
            print(f"{colors_dict['Reset']}")

            # If your response is acceptable
            if age.isdigit():

                # Turning your response into int variable
                age = int(age)

                # If your age is normal
                if age > 0:

                    user_dict["Age"] = age
                ###

                # If your age are strange
                else:
                    
                    # Show message
                    self.outScopeResponse(f"Sorry, I couldn't understand your answer :^( \nBut for now, let's assume you are {colors_dict['Reset']}{colors_dict['White']}16 years {colors_dict['Reset']}old...")

                    # Putting a acceptable value into user dictionary
                    user_dict["Age"] = 16
            ###

            # Else
            else:
                
                # Show message
                self.outScopeResponse(f"Sorry, I couldn't understand your answer :^( \nBut for now, let's assume you are {colors_dict['Reset']}{colors_dict['White']}16 years old...{colors_dict['Reset']}")

                # Putting a acceptable value into user dictionary
                user_dict["Age"] = 16
            ###
            
            # deleting the (NOW) useless variables
            del age
        ###
        
        # If it's 5º(and last) step conversation
        else:
            
            # Importing some libraries
            import getpass

            # Cleaning terminal
            self.terminalClear()
            
            # Showing text
            self.personSpeak("Thank you for providing the information!")
            self.personSpeak("From now on, you will also be a person, and as a person, you can interact with me...")
            self.personSpeak("Let's see?\n")

            # Waiting for response
            interaction = getpass.getpass(f"{user_dict['Color Itself']}Start!")

            # To reset font / break 1 line
            print(f"{colors_dict['Reset']}", end = "")

            # deleting the (NOW) useless libraries / variables
            del interaction, getpass
        ###
    ###

    # To person inputs
    def personAnswer(self) -> str:
        
        # Special font
        self.personSpeak("", "")

        # Getting value
        local_var = input(f"{styles_dict['User Response']}")

        # To break line / reset font
        print(colors_dict["Reset"], end = "")

        # returning value
        return local_var
    ###
###

# Creating the `Me` object
Me = Person("Pedro", "2004-04-29", "Blue", colors_dict["Blue"], "Brazil")

# Talking to you
for i in range(5):

    Me.autoConversation(i)
###

# Creating the `You` object
You = Person(user_dict["Name"], user_dict["Age"], user_dict["Color Name"], user_dict["Color Itself"], user_dict["Nationality"])

# Infinite Loop
while True:

    # Cleaning terminal
    Me.terminalClear()

    # Setting options
    options_box = ["Who I am?", "Ask my age?", "Quit interaction?"]

    # Asking
    Me.personSpeak("How do you want to interact?\n")

    # Showing options
    for option in range(3):

        Me.personSpeak("", end = "")
       
        print(f"{option + 1}. {options_box[option]}")
    ###
    
    # To break line
    print()
    
    # Getting value
    response = You.personAnswer()

    # To break line
    print()

    # Case response type != int
    if response.isdigit() == False:
        
        # Importing some libraries
        from time import sleep

        # Cleaning terminal
        Me.terminalClear()

        # Printing error text
        Me.outScopeResponse("Non acceptable response. \nThe interaction will end!", False)

        # Sleep time
        sleep(4)

        # deleting the (NOW) useless variables / libs
        del response, options_box, sleep

        # Breaking the loop
        break
    ###

    # Else
    else:

        # Turning response into int type
        response = int(response)

        # If response == out scope
        if response < 0 or response > 5:

            # Importing some libraries
            from time import sleep

            # Printing error text
            Me.outScopeResponse("Non acceptable response. \nThe interaction will end!", False)

            # Sleep time
            sleep(4)

            # deleting the (NOW) useless variables / lib
            del response, options_box, sleep

            # Breaking the loop
            break
        ###

        # Else
        else:

            # If ask == "Who I am?"
            if response == 1:

                # Importing some libraries
                from time import sleep

                # Cleaning terminal
                Me.terminalClear()

                # Answering
                Me.personSpeak(f"I'm {Me.name}, from {Me.nationality}!")

                # Sleep time
                sleep(2)

                # deleting the (NOW) useless library
                del sleep
            ###
            
            # If ask == "Ask my age?"
            elif response == 2:
                
                # Importing some libraries
                from time import sleep

                # Cleaning terminal
                Me.terminalClear()

                # Printing text
                Me.personSpeak(f"Are you {You.age} years old!? Cool, I'm {Me.age}.")

                # Sleep time
                sleep(2)

                # deleting the (NOW) useless library
                del sleep
            ###

            # If ask == "Quit interaction"
            elif response == 3:
                
                # Importing some libraries
                from time import sleep

                # Cleaning terminal
                Me.terminalClear()

                # Printign text
                Me.personSpeak(f"Ok. Bye, {You.color_itself}{You.name}!{colors_dict['Reset']}")

                # Sleep time
                sleep(2)

                # deleting the (NOW) useless library
                del sleep

                # Breaking loop
                break
            ###
        ###
    ###
###

# Final terminal clear
Me.terminalClear()

# Deleting some things
del Union, Me, You, Person

# Quitting
quit()