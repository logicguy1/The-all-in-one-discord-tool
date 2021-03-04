from colored import fg, attr
import requests
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def bumper():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {r2}[{b}?{r2}] Token: ")
    }

    id = input(f" {r2}[{b}?{r2}] Channel ID: ")
    print(f" {r2}[{b}!{r2}] Use ^C to exit")
    time.sleep(.3)
    print("")

    while True:
        requests.post(
            f"https://discord.com/api/channels/{id}/messages",
            headers = headers,
            json = {"content" : "!d bump"}
        )
        print(f" {r2}[{b}+{r2}] Server Bumped")
        time.sleep(121 * 60)
