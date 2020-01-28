
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  # Simply says hi, and then asks "what is my favorite color" before doing nothing else.
  - What do you think the program did with what you typed in answer to the question?
  # Program isn't coded to respond to anything, so it just did nothing. Exited out.

- Open main02.py. Before running it, describe how this is different than main01.py.
  # Unlike main01.py, this one has a bit of code that allows for a input box to appear in the terminal.
  - What do you think the color = input() will do?
  # Should allow me to type something in, where as before it would do nothing if I put anything in.
  - Run the program in the terminal and answer the question. Did the program do what you expected?
  # As expected, since it doesn't have anything to tell it to react in a certain way when I put something in, nothing happened. It has the input box, but cannot go any further.

- Open main03.py. Before running it, describe how this is different than main02.py.
  # Well, there is now code that tells the program to respond if the color "Red" is put in the box. Anything else, and it gives a message saying that the answer is wrong.
  - What is happening on lines 9–12?
  # If the color put in is "Red", then it will say "Correct". If it's anything that isn't "Red", then it will say "Sorry, try again."
  - Why are lines 10 and 12 indented?
  # Lines 10 and 12 are conditional. If the input is "Red", then it will print "Correct". Likewise with the [else] line- if it's not, it will say try again.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
  # Because it's coded to specifically say yes to "Red" with a capital "R", it will say no to everything else, including an uncapitalized "red".
  - What does this tell you about "color"?
  # Color has predefined... things? All the colors are punctuated properly, like "Red".

- Open main04.py. Before running it, describe how this is different than main03.py.
  # The program now accepts "Red" AND "red" as right answers. 
  - What problem is this trying to solve?
  # This makes an attempt to correct the previous program's problem, where it wouldn't accept the word "red", which is the exact same answer as "Red".
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
  # As expected, it only accepts the two defined answers. A janky "rEd", "REd" or "RED" won't be accepted as a right answer. It's the same situation as before.

- Open main05.py. What do you expect line 9 to do?
  # Now equipped with "lower", the program will now accept any form of the word "red".
  - What problem is it trying to solve?
  # Solves the issue of anyone who puts "red" in any weird way they want.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
  # Won't accept the "red " or any form of it with spaces before or after it. Because it then becomes a new "word", in a sense.

 - Open main06.py. How is line 9 different than in main05.py?
  # This line now has the "strip" bit in it.
   - What would you guess .strip() is doing?
  # Removes any extra spaces (intentional or unintentional) in the input of whatever is put in. In this case... red.
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
  # Spacing the letters in the word "red" out, like "re d" will break the logic.

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
  # Adds a new possible input choice- pink, and a new response illicited if it's entered into the input box.
   - What is happening on line 12?
  # If the answer is "pink", then it will give an answer that says "Close!"
   - Run the program and answer the question.
  # I'm not sure if I'm supposed to say anything on this line, but yes, if you put pink into the input box, it will say that you're close. Putting red in still works as normal.

 - Open main08.py. What is the purpose of line 9?
  # States that the color is red. Like... that's the correct answer.
   - Why are lines 10–17 indented?
  # This is a... conditional thing? While the answer is red, lines 10-17 are active.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
  # I... honestly have no idea.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
  # Ah, okay. It ends the program since the question is placed before the bits and bobs that make it actually work. Because they're now two separate lines, and there's no indentation, it's busted.

 - Open main09.py. What is happening on line 13?
  # The code that adds the amount of guesses taken.
   - What is the purpose of “count”?
  # Serves as a way to keep track of something, in this case, the amount of guesses.
   - What is happening on line 22?
  # Either I have a bad document, or maybe there's not anything supposed to be there. There is a "format count", which resets the count once the message that tells you how many tries it took is achieved.
   - Run the program.
  # ok

 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
  # ok

 - *Extra credit:* open main11.py. What is happening on lines 6-11?
  # So what this is, is the color selector, and it chooses from the list of predefined colors as to what will be the mystery color. However, it will NOT choose a color that was the answer previously.
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
