from colored import fg, attr
import requests
import threading
import time
import random

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def start():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")
    channel = input(f" {r2}[{b}?{r2}] Channel Id: ")

    def execute_command(command = "", cooldown = 0):
        print(f"{r2}[{b}!{r2} Loaded: '{command}' With cooldown of {cooldown} Seconds")
        while True:
            requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data = {'content': command},
                headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization' : token
                }
            )
            print(f"{r2}[{b}+{r2}] '{command}' Ran successfully")

            time.sleep(cooldown + random.randint(2, 10))

    commands = {
        "pls beg" : 45,
        "pls hunt" : 40,
        "pls fish" : 40,
        "pls daily" : 86400
    }

    print()

    for cmd, cooldown in commands.items():
        threading.Thread(target = execute_command, kwargs = {"command" : cmd, "cooldown" : cooldown}).start()
        time.sleep(5)
