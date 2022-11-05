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

fake_mult = Faker(["en_US", "lv_LV", "ja_JP", "es_MX", "ru_RU", "et_EE", "lt_LT"])
fake = Faker("en_US")

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clear()

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

con = Console()

options = Group(
    Panel("[black]1.[/black] Back",style="bold black on yellow"),
)
con.print(Panel(options),style="bold green")

targettable = Table(title="Targets", show_lines=True, box=box.SQUARE, style="bold red", justify="center", align=Align.CENTER, no_wrap=False, expand=True, highlight=True)


targettable.add_column("Name", style="bold red", no_wrap=False, justify="right")
targettable.add_column("Money", style="bold green", no_wrap=False, justify="right")
targettable.add_column("Address", style="bold blue", no_wrap=False, justify="right")
targettable.add_column("Occupation", style="bold magenta", no_wrap=False, justify="right")

for i in range(targetcount):
    targettable.add_row(targetlist[i], moneyamounts[i], targetaddresses[i], occupations[i], no_wrap=False)

con.print(targettable)