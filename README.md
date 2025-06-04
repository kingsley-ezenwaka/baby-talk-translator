# Baby-Talk Translator

## Description
This was my entry for the "Implement a text-to-baby-talk" challenge on [StackOverflow.com](https://stackoverflow.com/beta/challenges/79640866/79647869).

The challenge was quite simple: *Implement a program that translates any sample body of text up to 100 words into baby talk.*

My entry was Python code with a Tkinter GUI wrapper. It employs a dictionary of common baby words and a mix of character-switching functions to simulate baby speech (e.g. hello = "hewwo", pettishly = "teppishwy"). As a plus, the translated baby speech is coded to retain all punctuations and sentence-format from the source text. :)

See attached screenshot.

## To use:
If you already have Python installed, simply save the code block as a .py file and double-click on the file to run. It opens a simple tk window with an input textbox where you can enter the text to be translated, a "Translate to Baby-talk" button, and an output textbox that shows the translated baby-talk. There is also a "Clear" button to clear contents and enter new text.

Download and install Python from [the official home](https://www.python.org/downloads/).

### Sample Text Input
(from [Goldilocks and the Three Bears](https://learnwithhomer.com/library/story/goldilocks-and-the-three-bears) hosted on [learnwithhomer.com](https://learnwithhomer.com))
*After all that skipping, Goldilocks was starving. Goldilocks went to the table, where she found three bowls of porridge. She tasted the first bowl. “Too sweet!” she said. Then she tasted the middle bowl. “Too cinnamony!” she said. Finally she tasted the last bowl. It was just right! “Wow! This is delicious porridge!” she said.*

### Output
`After aww dat kipping, Gowdiwok was tawbing. Gowdiwok went to ve table, where she found dwee bowws of powwidge. She tasted ve first bowl. “Too sweet!” she said. Den she tasted ve middle bowl. “Too cinnamomie!” she said. Finawwy she tasted ve wast bowl. It was just wight! “Wow! Dis is dewicious powwidge!” she said.`

