from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import prompt
import asyncio

# Définition des commandes de complétion
COMMANDS = ["ls", "cd", "mkdir", "rm", "touch", "cat", "echo", "exit"]
completer = WordCompleter(COMMANDS)

class CommandPrompt(Input):
    """Un widget personnalisé pour la saisie de commande avec autocomplétion."""

    async def on_key(self, event):
        """Capture les entrées et affiche les suggestions de prompt_toolkit."""
        if event.key == "enter":
            # Traite la commande ici (affiche le texte par exemple)
            self.post_message(event.sender.text)
            self.text = ""

class TerminalApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Interface avec Textual et Prompt Toolkit", id="title")
        yield CommandPrompt(id="prompt")  # Zone de saisie de commandes
        yield Static("Résultats des commandes :", id="output")

    async def on_mount(self):
        self.output = self.query_one("#output")

    async def action_run_command(self, command_text):
        # Code pour exécuter la commande ou traiter le texte avec prompt_toolkit
        pass

    async def action_display_output(self, text):
        self.output.update(text)  # Affiche le texte dans la sortie

# Exécute l'application
if __name__ == "__main__":
    app = TerminalApp()
    app.run()
