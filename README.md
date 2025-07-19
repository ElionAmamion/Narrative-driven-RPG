# Narrative driven RPG - TEMPLATE
This is a template to easily create a narrative driven RPG game.

## functions.py
in this file are multiple functions usefull for creating a fluent story.
#### clear(waitingTime)
- sleeps for `waitingTime`
- prints `...`
- awaits user input
- clears on `Enter` the terminal
#### choice(tuple_options, count=("[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]", "[H]", "[I]"))
- prints `What do I choose`
- prints every element of `tuple_options` with a prefix from count
- awaits user input
- checks if answere is the same as one of the prefixes:
  - returns answer
- else:
  - returns `0`

#### dialogue(lines)
- prints every line of `list` `lines`
## dialogue.py
in this tile are all lists of dialogue stored

## Player.py
in this file is the `Player` class stored
### Player
#### __init__(Name, Health)
- stores `self.Name` and `self.Health`
#### __str__(self) and __repr__(self)
- return `f"{self.Name}, {self.Health}"`
