import code


def main():
    
    console = code.InteractiveConsole
    chaine = console.raw_input(console, prompt="bdhh $ ")
    print(f"La chaine que vous avez saisie est : {chaine}")


if __name__ == "__main__":
    main()