"""
Author:         Gavin Morgan
Date:           4/22/2024
Assignment:     Project 2
Course:         CPSC1050

Project Description:

"""

class ExitNotFoundError(Exception):
    
    #This initializes this exception class
    def __init__(self, exit_choice, message="Landing spot not found"):
        self.exit_choice = exit_choice
        self.message = message
        super().__init__(message)

#This is the actual message string of the exception
    def __str__(self):
        return f"{self.exit_choice} -> {self.message}"
    

class Room:
    #This is a function that initializes the variables in the class "Room"
    def __init__(self,name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

#This is a function that returns the room name
    def get_name(self):
        return self.name

#This is the function that returns the description of the room
    def get_description(self):
        return self.description

#Function where you can get the exits of the current room
    def get_exits(self):
        return self.exits
#Function of a list of the exits with a new line in between
    def list_exits(self):
        return '\n'.join(self.exits)
#This is the actual string printed whenever a room is entered
    def __str__(self):
        return f"{self.name}: {self.description}\n\nOther Locations:\n{self.list_exits()}"

class AdventureMap:
    #Initialize the map
    def __init__(self):
        self.map = {}
    
    #Funciton where rooms can be added to the map
    def add_room(self, room):
        self.map[room.name.lower()] = room
    #Function where if they choose an exit it will go to the exit if not an exception error occurs
    def get_room(self, name):
        room = self.map.get(name.lower())
        if room:
            return room
        else:
            raise ExitNotFoundError(name)
    


def main():
#All rooms are being added
    adventure_map = AdventureMap()
    adventure_map.add_room(Room("Titled Towers", "A city composed of several large skyscrapers with cramped interiors, each consisting of several stories, the tallest of which was a large clock tower", ['Greasy Grove']))
    adventure_map.add_room(Room("Pleasant Park", "The longest standing named location in Fortnite history, this place is a nice suburb town with plenty of houses and a soccer pitch.", ["Retail Row", "Retail Row", "Salty Springs"]))
    adventure_map.add_room(Room("Greasy Grove", "Notably known for the elegant Durrr Burger restaurant, there is also an outdoor equipment store and a gas station equipped with fantasic loot!", ["Salty Springs", "Tilted Towers"]))
    adventure_map.add_room(Room("Salty Springs", "This highly populated small residental area has above average loot, but make sure to check the attics!", ["Greasy Grove", "Pleasant Park", "Wailing Woods"]))
    adventure_map.add_room(Room("Retail Row", "Located northeast of Salty Springs,you will find a retail store with plenty of buildings and parking lots at this location.", ["Pleasant Park"]))
    adventure_map.add_room(Room("Loot Lake", "An island house surrounded by shallow lake water, there are various hidden secreted found here.", ["Wailing Woods", "Pleasant Park"]))
    adventure_map.add_room(Room("Wailing Woods", "You've came to the perfect spot to collect materials. The biggest forested area on the map, these thick rooted woods of provide great shelter but not much desired loot.", ["Salty Springs", "Retail Row"]))

    #Starting statement and starting the game in the study room
    print("\nWelcome to Fortnite! The Bus has dropped you off at a hot spot, named Salty Springs! To finish looting/traveling to locations, please type exit to hop back on the battle bus.\n")
    the_room = adventure_map.get_room("Salty Springs")
    
    
    print(the_room)

    choice = 'play'

    while choice != 'exit':
        try:
            print()
            #Asks for an exit and takes in an input 
            print("Please choose an exit: ")
            exit_choice = input().title().strip()
            
            #Checks to see if user wants to end the game, if so it breaks out of the game loop
            if exit_choice.lower() == 'exit':
                choice = 'exit'
                break
            
            #If they choose a valid exit, the room they chose is now the current room
            if exit_choice in the_room.get_exits():
                the_room = adventure_map.get_room(exit_choice)
                print(the_room)
                
            #If not a valid exit an error is raised so our exception class can be called
            else:
                if exit_choice not in the_room.get_exits():
                   raise ExitNotFoundError(exit_choice)
            
        except ExitNotFoundError as e:
            print(e)
    #Final statement once the user decides to end the game.
    print("The battle bus has passed by to pick you up... thanks for coming to Fortnite's Battle Royale Island!")

    if __name__ == "__main__":
        main()