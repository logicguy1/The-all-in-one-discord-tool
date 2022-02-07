LICENSE = """
Copyright © 2021 Drillenissen#0666
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg
import requests
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def spammer():
    webhook = input(f"\n {r2}[{b}?{r2}] Webhook URL: ")
    message = input(f" {r2}[{b}?{r2}] Message: ")
    timer = input(f" {r2}[{b}?{r2}] Amount of time between attack(s): ")
    print("")

    timeout = time.time() + 1 * float(timer) + 2

    while time.time() < timeout:
        response = requests.post( # Send the webhook message
            webhook,
            json = {"content" : message},
            params = {'wait' : True}
        )

        if response.status_code == 204 or response.status_code == 200:
            print(f" {r2}[{b}+{r2}] Message Sent")
        elif response.status_code == 429:
            print(f" {r2}[{b}-{r2}] Rate Limited ({response.json()['retry_after']}ms)")
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(f" {r2}[{b}-{r2}] Error Code: {response.status_code}")

        time.sleep(.5)
