## Python Warrior Player

This repo contains my base Player class for the [python-warrior](https://github.com/arbylee/python-warrior) game.

This is a very fun game, made to teach python and the very basics of artifial inteligence. You write code to help the warrior determine and execute his actions, defeat enemies and rescue captives on a dungeon.

The code makes the warrior reach the top of the tower and rescue the fair maiden :snake: Python in EPIC mode at the beginner level(once you cross that bridge there's more challeging levels), but that's good enough for now 🙂.

### Running locally

To run it and confirm everything works, just create a venv with `python -m venv .venv` install the requirements with `pip install -r requirements.txt` and finally run `pytest` on the top level directory on this project. This will run every level of the game one by one, regardless of the mode(epic, default), so you can make modifications and see which levels fail or continue to pass.