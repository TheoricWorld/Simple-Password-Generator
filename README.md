# **Simple Password Generator**

## Table of Contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Dependencies](#dependencies)
* [How to use?](#how-to-use)
* [Logic Diagram of the project](#logic-diagram-of-the-project)
* [Modifiying values](#modifiying-values)
* [Status](#status)

## General info
A simple password generator with Graphic User Interface using Object-oriented programming as a practice of the subject.

## Screenshots
![MainMenu](https://i.imgur.com/OmLT4r4.jpg)
![ExampleShort](https://i.imgur.com/ys5vEk2.jpg)
![ExampleCopy](https://i.imgur.com/dhYeEPk.jpg)
![ExamplePaste](https://i.imgur.com/tcoo274.jpg)
![ExampleLong](https://i.imgur.com/Hm9d9Z1.jpg)

##  Technologies
Project developed with Python and the following libraries:
* String
* Random
* Tkinter
* Ttk 

## Features
* Easy code to modified (or that is what I have intended).
* Chance rate on the type of character.

## Dependencies
Make sure you have installed the font: **Argentum Sans Regular**. If it is not your case, you can install it from [here](https://www.1001fonts.com/argentum-sans-font.html) or replace it with another one you already have as **Helvetica** from the view.py file (Line: 47). 

## How to use?
It is very intuitive and simple:
1. Run the view.py file with Python Interpreter or use the .exe version of it.
2. Select the lenght of the password:

    | Length      | Number of characters |
    | :----:  | :----:  |
    | Short       | 6         |
    | Medium      | 8         |
    | Large       | 12        |
    | Extra Large | 16        |

3. Press **Generate** button.
4. In the textbox will appear a random password with the length you have choosen. 
5. If you want to use that password, you can press the **Copy** button to "Copy to clipboard" (A message will be displayed that it is already copied).
6. Otherwise, you can generate a new password with the same or a different length until you get satisfied.

## Logic Diagram of the project
![LogicDiagram](https://i.imgur.com/jUrJUI7.png)

## Modifiying values
At utility.py file you can easily modified the length values of the project (so you can make the range of characters shorter or larger). 

| Constant  | Value  |
| :----:    | :----: |
| LENGTH_S  | 6      |
| LENGTH_M  | 8      |
| LENGTH_L  | 12     |
| LENGTH_XL | 16     |

Additionally, you can modify the rate/probability of getting a random letter, punctuacion or digit character.

In this case, a hundred samples of random passwords were taken from [LastPass](https://www.lastpass.com/password-generator) to make sure that the generator does not abuse of punctuation or digits characters.

After a simple statistical analysis it can be stated that:
* Around 69% of the characters were letters.
* Nearly 21% were punctuation characters.
* Only 10% were digits. 

With this information, you can modified the initial value of getting a letter to the rate you want. Then, you have to sum the probability value of get a punctuation character to this initial value (this will be the punctuation value you have to modified). Finally, the digit rate will always be 100 (because it will automatically fit with the missing rate).

## Status
Project is: _finished_.

However, there are widely ideas to improve the current project and make it more attractive (especially in the UI design).