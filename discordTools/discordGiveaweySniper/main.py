import json
import time
import bot
import os

class Sniper:
    def main(self): # Main function, holds the main code
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """) # Print the title card

        time.sleep(2) # Wait a few seconds
        self.slowType("Made by: Drillenissen#4268 && Benz#4947", .02) # Print who developed the code
        time.sleep(1) # Wait a little more
        self.slowType("\nInput your Discord token: ", .02, newLine = False)
        token = input("") # Get the discord token

        self.slowType("\nDo you wish to use AutoBump? (Y/n): ", .02, newLine = False) # Ask if they want to use autobump
        bumper = input("") # Wait for an awnser

        if "y" in bumper.lower(): # If y is in the responce
            bumpData = self.setupBump() # Run the setup code for auto bump
        else: # If there is no y in the responce
            bumpData = None # Let the bot know it does not have to start the loop

        with open("dataPass", "w") as josnFile: # Open the file used to pass data into the bot
            json.dump( # Dump the requed data
                {"snipeToken" : token, "bumpServers" : bumpData},
                josnFile
            )

        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

        self.start(token) # Start the bot using the start code

    def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

    def setupBump(self): # Used to get the data needed
        # Give the users the instructions
        self.slowType("Input a guild ID and channel ID ( Split with a space ) and stop to stop", .02)
        bumpInfo = [] # List used to keep track of the servers and channels that should be autobumped

        while True: # Loop untill break
            bumpInfoRaw = input(">>> ").strip() # Ask the user for the channel and guild ids

            if bumpInfoRaw.lower() == "stop": # If the responce is "stop"
                break # Stop the loop

            bumpInfo.append( # Otherwise give the bumpInfo list the information it needes
                {
                    "guildId" : bumpInfoRaw.split(" ")[0],
                    "channelId" : bumpInfoRaw.split(" ")[1]
                }
            )

        return bumpInfo # Return that to the main function

    def start(self, token): # Function used to start the main bot
        Bot = bot.bot # Initialise the bot object ( This is a discord bot )

        Bot.run( # Run the bot with the token etc
            token,
            bot = False,
            reconnect = True
        )

if __name__ == '__main__': # If the file is getting ran directly
    NitroSniper = Sniper() # Create the sniper class
    NitroSniper.main() # Run the main function
