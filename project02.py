"""
Author:         Gavin Morgan
Date:           4/22/2024
Assignment:     Project 2
Course:         CPSC1050

Project Description: This project outlines a game similar to fortnite, where the user choosing landing spots, items to pick up and use in a inventory, as well as maintaining health/survive.

"""
class Health:
    def __init__(self):
        self.health = 100

    def lose(self,amount):
        self.health -= amount
    
    def gain(self,amount):
        self.health += amount

    def get(self):
        return self.health
        
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
        return f"{self.name}: {self.description}\n\nLocations:\n{self.list_exits()}"

class AdventureMap:
    #Initialize the map
    def __init__(self):
        self.map = {}
    
    #Funciton where rooms can be added to the map
    def add_place(self, room):
        self.map[room.name.lower()] = room
    #Function where if they choose an exit it will go to the exit if not an exception error occurs
    def get_place(self, name):
        room = self.map.get(name.lower())
        if room:
            return room
        else:
            raise ExitNotFoundError(name)


    
class Inventory:
    # Iniitalize inventory
    def __init__(self):
        self.items = []

    # adds item to inventory
    def obtain(self,item):
        self.items.append(item)

    # determines if item is in inventory or not
    def get_item(self,item):
        if item in self.items:
            return True
        else:
            return False


    #def use_item(self,item):
    #    if item in self.items:
    #        self.items.remove(item)
    #        return True
    #    else:
    #        return False
        



def main():
    adventure_map = AdventureMap()
    inventory = Inventory()
    health = Health()
    #All rooms are being added
    adventure_map.add_place(Room("Tilted Towers", "A city composed of several large skyscrapers with cramped interiors, each consisting of several stories, the tallest of which was a large clock tower", ['Greasy Grove']))
    adventure_map.add_place(Room("Pleasant Park", "The longest standing named location in Fortnite history, this place is a nice suburb town with plenty of houses and a soccer pitch.", ["Retail Row", "Wailing Woods", "Salty Springs"]))
    adventure_map.add_place(Room("Greasy Grove", "Notably known for the elegant Durrr Burger restaurant, there is also an outdoor equipment store and a gas station equipped with fantasic loot!", ["Salty Springs", "Tilted Towers"]))
    adventure_map.add_place(Room("Salty Springs", "This highly populated small residental area has above average loot, but make sure to check the attics!", ["Greasy Grove", "Pleasant Park", "Wailing Woods"]))
    adventure_map.add_place(Room("Retail Row", "Located northeast of Salty Springs, you will find a retail store with plenty of buildings and parking lots at this location.", ["Pleasant Park"]))
    #adventure_map.add_room(Room("Loot Lake", "An island house surrounded by shallow lake water, there are various hidden secreted found here.", ["Wailing Woods", "Pleasant Park"]))
    adventure_map.add_place(Room("Wailing Woods", "You've came to the perfect spot to collect materials. The biggest forested area on the map, these thick rooted woods provide great shelter but not much desired loot.", ["Salty Springs", "Retail Row"]))

    #Starting statement and starting the game in the study room
    print("\nWelcome to Fortnite!")
    print('Aviod running out of health, and reach a health of 160 to obtain full potential/win!  ')
    print()
    name = '1'
    while name.isdigit() == True:
        print('Before playing, enter a username (cannot be all digits): ',end='')
        name = input().strip()

    print('\nThe Bus has dropped you off at a hot spot, named Salty Springs! To finish looting/traveling to locations, please type exit to hop back on the battle bus.\n')
    
    print('This highly populated small residental area has above average loot, but make sure to check the attics!')
    #the_room = adventure_map.get_place("Salty Springs")
    #print(the_room)
    print('\nWhat item would you like to pickup? Rift To Go, Grenade, Grappler: ',end='')
    action_ = input().lower().strip()
    action = action_.title()
    the_item = inventory.get_item(action)

    if the_item:
        print('\nYou have already used this item. You have failed to pay attention!\n')
        print('Lose 10 health')
        health.lose(10)
    
    elif action == 'Rift To Go':
        inventory.obtain('Rift To Go')
        print('\nYou used the Rift To Go, escaping a massive build fight of 8 players!')
        print('Your health remains the same')
    
    elif action == 'Grenade':
        inventory.obtain('Grenade')
        print('\nAfter activiting the grenade, you held it for too long. This has caused significant body damage.')
        print('Lose 90 health') 
        health.lose(90)                
    
    elif action == 'Grappler':
        inventory.obtain('Grappler')
        print('\nThis came just at the right time, helping you avoid taking any storm damage.')
        print('Gain 10 health')
        health.gain(10)

    else:
        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
        print('Lose 25 health')
        health.lose(25)
    currentHealth = health.get()
    print('Health:',currentHealth)

    print('\n\nLocations:')
    print('Greasy Grove')
    print('Pleasant Park')
    print('Wailing Woods')
    








    choice = 'play'
    while choice != 'exit':
        try:
            print()
            #Asks for an exit and takes in an input 
            print("Please choose a location: ",end='')
            exit_choice = input().title().strip()
            the_room = adventure_map.get_place(exit_choice)
            
            #Checks to see if user wants to end the game, if so it breaks out of the game loop
            if exit_choice.lower() == 'exit':
                choice = 'exit'
                #Final statement once the user decides to end the game.
                print("The battle bus has passed by to pick you up early. Come back to Fortnite's Battle Royale Island again when your up for the challenge!")
                break

            if exit_choice in the_room.get_exits():
                
                #the_room = adventure_map.get_place(exit_choice)
                print()
                print(the_room)
                #print('Locations:\n')
                #options = 

                # TILTED TOWERS 
                if exit_choice == 'Tilted Towers':
                    print('What item would you like to pickup? Freeze Trap, Berries, Pistol: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action)
                    
                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Freeze Trap':
                        inventory.obtain('Freeze Trap')
                        print('\nYou have by accidently used the freeze trap, causing you to slide into a thorn bush.')
                        print('Lose 15 health')
                        health.lose(15)
                    
                    elif action == 'Berries':
                        inventory.obtain('Berries')
                        print('\nThe berries looked suspicious, but you ate them anyway. Luckily they were digested well.')
                        print('Gain 25 health')
                        health.gain(25)
                    
                    elif action == 'Pistol':
                        inventory.obtain('Pistol')
                        print('\nYou have found a rusted pistol. Unfortunately it is unusable.')
                        print('Your health remains the same')  
                    
                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)

                
                # PLEASANT PARK 
                elif exit_choice == 'Pleasant Park':
                    print('What item would you like to pickup? Mini Shield, Wood, Pump Shotgun: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action) 
                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Mini Shield':
                        inventory.obtain('Mini Shield')
                        print('\nThis refreshing blue drink gave you just what you needed.')
                        print('Gain 25 health')
                        health.gain(25)
                    
                    elif action == 'Wood':
                        inventory.obtain('Wood')
                        print('\nYou have built yourself some temporary shelter out of wood, saving yourself from enemies.')
                        print('Gain 10 health') 
                        health.gain(10)                
                    
                    elif action == 'Pump Shotgun':
                        inventory.obtain('Pump Shotgun')
                        print('\nYou test out the newly obtained shotgun, but the recoil of the gun causes an injury.')
                        print('Lose 20 health')
                        health.lose(20)

                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)


                # GREASY GROVE
                elif exit_choice == 'Greasy Grove':
                    print('What item would you like to pickup? Rocket Launcher, Bandages, Sniper Rifle: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action)

                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Rocket Launcher':
                        inventory.obtain('Rocket Launcher')
                        print('\nYou have blown up 5 enemies that were coming your direction!')
                        print('Gain 20 health')
                        health.gain(20)
                    
                    elif action == 'Bandages':
                        inventory.obtain('Bandages')
                        print('\nWhat you thought would heal any wounds, these bandages were infected with various diseases.')
                        print('Lose 30 health') 
                        health.lose(30)              
                    
                    elif action == 'Sniper Rifle':
                        inventory.obtain('Sniper Rifle')
                        print('\nAfter picking up the rifle, you managed to hit a 250m snipe. Great work!')
                        print('gain 25 health')
                        health.gain(25)
                
                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)
                

                # SALTY SPRINGS
                elif exit_choice == 'Salty Springs':
                    print('What item would you like to pickup? Rift To Go, Grenade, Grappler: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action)

                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Rift To Go':
                        inventory.obtain('Rift To Go')
                        print('\nYou used the Rift To Go, escaping a massive build fight of 8 players!')
                        print('Your health remains the same')
                    
                    elif action == 'Grenade':
                        inventory.obtain('Grenade')
                        print('\nAfter activiting the grenade, you held it for too long. This has caused significant body damage.')
                        print('Lose 90 health') 
                        health.lose(90)                
                    
                    elif action == 'Grappler':
                        inventory.obtain('Grappler')
                        print('\nThis came just at the right time, helping you avoid taking any storm damage.')
                        print('Gain 10 health')
                        health.gain(10)
                
                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)
                

                # Retail Row
                if exit_choice == 'Retail Row':
                    print('What item would you like to pickup? Big Shield, Scar, Boogie Bomb: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action)  
                    
                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Big Shield':
                        inventory.obtain('Big Shield')
                        print('\nThis blue liquid was not what you thought, as it has been spiked with bad substances.')
                        print('Lose 50 health')
                        health.lose(50)
                    
                    elif action == 'Scar':
                        inventory.obtain('Scar')
                        print('\nYou have gotten arguably the best weapon in the game. Your skills have improvement significantly.')
                        print('Gain 35 health') 
                        health.gain(35)                
                    
                    elif action == 'Boogie Bomb':
                        inventory.obtain('Boogie Bomb')
                        print('\nYou must be in a great mood, enjoy your dance party with this item!')
                        print('Gain 20 health')
                        health.gain(20)
                
                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)


                # WAILING WOODS     
                if exit_choice == 'Wailing Woods':
                    print('What item would you like to pickup? Scoped AR, Fishing Rod, Shopping Cart: ',end='')
                    action_ = input().lower().strip()
                    action = action_.title()
                    the_item = inventory.get_item(action)  
                    
                    if the_item:
                        print('\nYou have already used this item. You have failed to pay attention!\n')
                        print('Lose 10 health')
                        health.lose(10)
                    
                    elif action == 'Scoped AR':
                        inventory.obtain('Scoped AR')
                        print('\nYou may have been hesitant to pick this up, but you lucked out. This is a mythic Scoped AR!')
                        print('Gain 45 health')
                        health.gain(45)
                    
                    elif action == 'Fishing Rod':
                        inventory.obtain('Fishing Rod')
                        print('\nSit back, relax, and see what you can reel in from the ocean found on the cost of Wailing Woods.')
                        print('Gain 10 health') 
                        health.gain(10)                
                    
                    elif action == 'Shopping Cart':
                        inventory.obtain('Shopping Cart')
                        print('\nUsing the shopping cart to gain some speed, you find yourself smashing into a massive tree stump.')
                        print('Lose 30 health')
                        health.lose(30)
                
                    else:
                        print('\nYou have taken a hit to your health for not chosing a proper item. The items have vanished and you are hit by a hidden spike trap on your way out.')
                        print('Lose 25 health')
                        health.lose(25)
                    
                currentHealth = health.get()
                if currentHealth <= 0:
                    print('Health: 0')
                    print('You have died! Better luck next time.')
                    break
                elif currentHealth >= 150:
                    print('Health:',currentHealth)
                    print('You reached a health above 150, reaching your full potential!')
                    print('You have won!')
                    print("\nThe battle bus has passed by to pick you up... thanks for coming to Fortnite's Battle Royale Island!")
                    break
                else:
                    print('Health:',currentHealth)
    
                
            #If not a valid exit an error is raised so our exception class can be called
            else:
                if exit_choice not in the_room.get_exits():
                   raise ExitNotFoundError(exit_choice)
    
        except ExitNotFoundError as e:
            print(e)

    #print(f'\n{name},Did you have fun playing the game? (Y/N): ',end='')    
    #final_feel = input().upper()
    #while final_feel != 'Y' or final_feeel != 'N':
    #    print(f'{name}, Please input a valid response (Y/N): ',end='')
    #    final_feel = input().upper()
    
    #if final_feel == 'Y':
    #    print('\nI am gald you enjoyed the game!!!')
    #elif final_feel == 'N':
    #    print('\nI hope you have a better time next time around.')

if __name__ == "__main__":
    main()