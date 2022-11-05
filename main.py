import pyfiglet
from rich.console import Console
from rich.console import Group
from rich.panel import Panel
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from mnemonic import Mnemonic
mnemo = Mnemonic("english")
from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.align import Align
from faker import Faker
from faker.providers import person
from random import randint
import pygame

pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load("audioname") 
# pygame.mixer.music.play()

fake_mult = Faker(["en_US", "lv_LV", "ja_JP", "es_MX", "ru_RU", "et_EE", "lt_LT"])
fake = Faker("en_US")

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clear()

if os.path.exists("lockdown_code.txt"):
    os.remove("lockdown_code.txt")

services={
    "service_1" : True,
    "service_2" : True,
    "service_3" : True,
    "service_4" : True,
    "service_5" : True,
    "service_6" : True,
}

servicecolors = {
    "service_1" : "",
    "service_2" : "",
    "service_3" : "",
    "service_4" : "",
    "service_5" : "",
    "service_6" : "",
}


# Service 1 settings
service1_lockdown = False
# Service 2 settings

# Service 3 settings

# Service 4 settings

# Service 5 settings

# Service 6 list of targets generator.
targetlist = []
moneyamounts = []
targetaddresses = []
occupations = []

targetcount = randint(3,16)
countie = 1
for _ in range(targetcount):
    cashamount = randint(5000, 100000)
    fullname = fake_mult.name()
    targetaddress = fake.address()
    occupation = fake.job()
    formatted_cashamount = "${:,.2f}".format(cashamount)
    targetlist.append(fullname)
    moneyamounts.append(formatted_cashamount)
    targetaddresses.append(targetaddress)
    occupations.append(occupation)
    countie += 1



# Set console and make banner with Pyfiglet
con = Console()
banner = pyfiglet.figlet_format(" ScarNet",font="fender") # extra font choices: banner3-D and nancyj-fancy


##################################################
##############       START        ################
##################################################

def start():
    
    clear()
    print()
    con.print(banner,"Scarlet Network.\n",style="bold red",highlight=False)
    for i in services:
        if services[i] == True:
            con.print(f"{i}: [green]online[/green].")
            servicecolors[i] = "bold green"
        else:
            con.print(f"{i}: [red]offline[/red].")
            servicecolors[i] = "bold red"

    if service1_lockdown == True:
        servicespanels = Group(
        Panel("[yellow]1.[/yellow] Manage [white]Lockdown[/white] on network.",style=servicecolors["service_1"]),
        Panel("[white]2.[/white] Settings",style="bold yellow"),
        )
        con.print(f"\n[red]Lockdown:[/red] [green]ON[/green]",style="bold red", justify="center")
        con.print(Panel(servicespanels),style="on red")
        def askInt():
            answer = IntPrompt.ask("(Selected Service)",choices=['1','2'])
            if answer == 1:
                if services["service_1"] == True:
                    service1()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 2:
                settings()

        askInt()
    else:
        servicespanels = Group(
        Panel("[yellow]1.[/yellow] Manage [red]Lockdown[/red] on network.",style=servicecolors["service_1"]),
        Panel("[yellow]2.[/yellow] EXPOSE [red]ScarNet[/red] SECRETS.",style=servicecolors["service_2"]),
        Panel("[yellow]3.[/yellow] Social Engineering Kit",style=servicecolors["service_3"]),
        Panel("[yellow]4.[/yellow] Brute Force Kit",style=servicecolors["service_4"]),
        Panel("[yellow]5.[/yellow] Wi-Fi Br3ach",style=servicecolors["service_5"]),
        Panel("[yellow]6.[/yellow] List of Targets",style=servicecolors["service_6"]),
        Panel("[white]7.[/white] Settings",style="bold yellow"),
        )
        con.print(Panel(servicespanels),style="bold green")
        def askInt():
            answer = IntPrompt.ask("(Selected Service)",choices=['1','2','3','4','5','6','7'])
            if answer == 1:
                if services["service_1"] == True:
                    service1()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 2:
                if services["service_2"] == True:
                    service2()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 3:
                if services["service_3"] == True:
                    con.print("[green]Service is [white]online[/white] but currently unavailable.[/green]")
                    askInt()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 4:
                if services["service_4"] == True:
                    con.print("[green]Service is [white]online[/white] but currently unavailable.[/green]")
                    askInt()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 5:
                if services["service_5"] == True:
                    con.print("[green]Service is [white]online[/white] but currently unavailable.[/green]")
                    askInt()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 6:
                if services["service_6"] == True:
                    service6()
                else:
                    con.print("[red]Service is offline.[/red]")
                    askInt()
            elif answer == 7:
                settings()
        askInt()

##################################################
##############      SETTINGS      ################
##################################################

def settings():
    clear()
    print()
    con.print(banner,"Scarlet Network.\n",style="bold red",highlight=False)
    for i in services:
        if services[i] == True:
            servicecolors[i] = "bold green"
        else:
            servicecolors[i] = "bold red"
    print("\n")
    con.print("Here you can enable/disable services.",style="bold cyan", justify="center")
    con.print("Simply type the service's order number and hit enter.\n",style="bold green", justify="center")
    con.print("SETTINGS",style="black on yellow blink", justify="center")
    servicespanels = Group(
        Panel("[yellow]1.[/yellow] Manage [red]Lockdown[/red] on network.",title="[red]Cannot disable if on lockdown![/red]",style=servicecolors["service_1"]),
        Panel("[yellow]2.[/yellow] EXPOSE [red]ScarNet[/red] SECRETS.",style=servicecolors["service_2"]),
        Panel("[yellow]3.[/yellow] Social Engineering Kit",style=servicecolors["service_3"]),
        Panel("[yellow]4.[/yellow] Brute Force Kit",style=servicecolors["service_4"]),
        Panel("[yellow]5.[/yellow] Wi-Fi Br3ach",style=servicecolors["service_5"]),
        Panel("[yellow]6.[/yellow] List of Targets",style=servicecolors["service_6"]),
        Panel("[black]7.[/black] Back",style="bold black on yellow"),
    )
    con.print(Panel(servicespanels),style="bold yellow")

    answer = IntPrompt.ask("(Selected Service)",choices=['1','2','3','4','5','6','7'])

    if answer == 1:
        if service1_lockdown == True:
            settings()
        else:
            services["service_1"] = not services["service_1"]
            settings()
    elif answer == 2:
        services["service_2"] = not services["service_2"]
        settings()
    elif answer == 3:
        services["service_3"] = not services["service_3"]
        settings()
    elif answer == 4:
        services["service_4"] = not services["service_4"]
        settings() #usa____
    elif answer == 5:
        services["service_5"] = not services["service_5"]
        settings()
    elif answer == 6:
        services["service_6"] = not services["service_6"]
        settings()
    elif answer == 7:
        start()

##################################################
##############     SERVICE 1      ################
##################################################

def service1():
    clear()
    print()
    con.print(banner,"Scarlet Network.\n",style="bold red",highlight=False)
    print()
    con.print("This is the toggle for [underline]LOCKDOWN[/underline].",style="bold cyan", justify="center")
    con.print("If on, all other services will be unusable.",style="bold red", justify="center")
    con.print("To disable the lockdown\nyou will need to enter a special code.\n",style="bold white", justify="center")
    con.print("LOCKDOWN TOGGLE",style="white on red blink", justify="center")

    if service1_lockdown == True:
        lockdown_color = "bold green"
        lockdown_message = "[white]2. [blink]LOCKDOWN[/white] ENABLED[/blink] [yellow](Unlock code is stored in [white]lockdown_code.txt[/white])[/yellow]"
        lockdown_code = randint(1000,9999)
        lockdown_code = str(lockdown_code)
        codebanner = pyfiglet.figlet_format(lockdown_code,font="top_duck")
        f = open("lockdown_code.txt", "w")
        f.write("LOCKDOWN UNLOCK CODE: \n\n" + codebanner + "Use this code to unlock the lockdown.\nEvery failed code attempt resets this code.\nIf that happens, reopen this file.")
        f.close()
    else:
        lockdown_color = "bold red"
        lockdown_message = "[white]2. LOCKDOWN[/white] DISABLED"

    options = Group(
        Panel("[black]1.[/black] Back",style="bold black on yellow"),
        Panel(lockdown_message,style=lockdown_color),
    )
    con.print(Panel(options),style="bold red")

    def askInt():
        global service1_lockdown
        answer = IntPrompt.ask("(Selected Option)",choices=['1','2'])

        if answer == 1:
            start()
        elif answer == 2:
            if service1_lockdown == True:
                answer = Prompt.ask("[red]Enter lockdown unlock code[/red]")
                if answer == lockdown_code:
                    service1_lockdown = False
                    f = open("lockdown_code.txt", "w")
                    f.write("LOCKDOWN UNLOCK CODE: \n\n" + pyfiglet.figlet_format("OFF",font="big") + "There is no code for you to use right now.") # extra font: top_duck
                    f.close()
                    service1()
                else:
                    service1()
            else:
                service1_lockdown = not service1_lockdown
                service1()

    askInt()

##################################################
##############     SERVICE 2      ################
##################################################

def service2():
    clear()
    print()
    con.print(banner,"Scarlet Network.\n",style="bold red",highlight=False)
    print()
    con.print("SENDER: [red]Unknown[/red]", justify="center")
    con.print("TIME: [yellow]Now[/yellow]", justify="center")
    print()
    con.print("NOW PLAYING: [green]A kind message[/green]",style="blink", justify="center")

    pygame.mixer.music.load("assets/audio.wav") 
    sleep(1)
    pygame.mixer.music.play()
    sleep(0.5)
    con.print("\n[yellow]TRANSCRIPT:[/yellow]")
    print("\nRight, I'll tell you what, you fat little ****,")
    sleep(2.3)
    print("You're borin', you don't sound Nigerian at all,")
    sleep(3.2)
    print("So.. go **** yourself...")
    sleep(2)
    print("GO ******* CRAWL IN A DIRTY, DANK LITTLE HOLE")
    sleep(2.7)
    print("WHERE YOU ******* COME FROM")
    sleep(1.45)
    print("YOU DIRTY ****** *****' LITTLE ******* SPASTIC")
    sleep(4.3)
    print("\nRight, OK, the 'dragon' comment")
    sleep(1.5)
    print("was probably a little bit ******* over-the-top")
    sleep(2.6)
    print("but at the end of the day")
    sleep(0.9)
    print("You're ******* borin'.\n")
    sleep(1.5)

    options = Group(
        Panel("[black]1.[/black] Back",style="bold black on yellow"),
    )
    
    con.print(Panel(options),style="bold red")

    def askInt():
        global service1_lockdown
        answer = IntPrompt.ask("(Selected Option)",choices=['1'])

        if answer == 1:
            start()

    askInt()


##################################################
##############     SERVICE 6      ################
##################################################

def service6():
    clear()
    print()
    con.print(banner,"Scarlet Network.\n",style="bold red",highlight=False)
    print("\n")
    con.print("Here is your HITLIST. You can do contracts here.",style="bold cyan", justify="center")
    con.print("This list refreshes periodically.\n",style="bold green", justify="center")
    con.print("TARGET LIST",style="white on green blink", justify="center")

    options = Group(
        Panel("[black]1.[/black] Back",style="bold black on yellow"),
    )
    con.print(Panel(options),style="bold green")

    targettable = Table(title="Targets", show_lines=True, box=box.SQUARE, style="bold red")


    targettable.add_column("Name", style="bold red", no_wrap=True, justify="right")
    targettable.add_column("Money", style="bold green", no_wrap=True, justify="right")
    targettable.add_column("Address", style="bold blue", no_wrap=True, justify="right")
    targettable.add_column("Occupation", style="bold magenta", no_wrap=True, justify="right")

    for i in range(targetcount):
        targettable.add_row(targetlist[i], moneyamounts[i], targetaddresses[i], occupations[i])

    con.print(targettable)

    def askInt():
        global service1_lockdown
        answer = IntPrompt.ask("(Selected Option)",choices=['1'])

        if answer == 1:
            start()

    askInt()


start()
