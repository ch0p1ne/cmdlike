import click
import sys
import os
import time
import socket
from rich.progress import track
from rich import print
from rich.layout import Layout
import pathlib


#from colorama import just_fix_windows_console
#from termcolor import colored

from rich.console import Console
from rich.text import Text

#necessaire pour les couleur sur terminal Windows
#just_fix_windows_console()

#commande personnaliser 
@click.command()
def coloured():
    click.secho('Hello there', fg="blue", bold=True)

def init():
    os.system("cls") 

def main():
    console = Console()

    try :
        init()

        
        console.print("This is text. ", style="bold underline green")
        console.print("[bold]This [cyan]is[/] some text. [/]")

        text = Text("Hello, world")
        text.stylize("bold magenta" , 0 , 6)
        console.print(text)
        console.print("Visit my [link=https://www.willmcgugan.com]blog[/link]  c'est un lien ! :warning-emoji: ")
        
        #for i in track(range(20), description="Processing..."):
        #   time.sleep(1)  # Simulate work being done

        
    

         #boucle principal du programme REPL (read - evaluate - print - loop)
        while True:

            hostName = Text(socket.gethostname())
            hostName.stylize("italic magenta")
            currentPath = pathlib.Path().absolute()
            console.print(f"\n  :green_circle: {hostName} :ice: {currentPath}  ")
            _in = console.input("\n\t:zap: ")
            #print(f"{_in}")


            ## un parcour dans un dictionnaire de commande par exemple
            if eval("_in == \"exit\""):
                break
            elif eval("_in == \"coloured\" "):
                coloured()
            else:
                os.system(_in)



    except Exception as e:
        print(f"\nError : {e}")



if __name__ == '__main__':
    main()
