# Wordifyery
### Simple terminal game for two players in guessing the word
* [How To Play](#How-To-Play)
* [Installation and Build](#Installation-and-Build)
  * [Install](#Install)
  * [Build](#Build)

## How To Play

This is a game for two players. One set a word - the other tries to guess it.

<img width="686" height="73" alt="Снимок экрана 2025-09-11 в 20 51 11" src="https://github.com/user-attachments/assets/991275f1-b1df-463e-9842-eae90cd3d930" />


The guesser has a certain number of attempts, which can be set by the argument "-L {number }". If the letter is in the word, it will be shown in yellow, if it is in place, it will be shown in green, and if the letter is not in the word, it will be shown in red.

<img width="684" height="169" alt="Снимок экрана 2025-09-11 в 20 57 58" src="https://github.com/user-attachments/assets/8f91e166-5864-4121-9cf3-ae185563f1c5" />


The "-T {number }" argument allows you to set the maximum number of tips. Hints reveal a random letter in a word, but they can only reveal letters until there are only 2 unknown letters left in the word. Guesser can use the tip by "!tip" command.

<img width="684" height="163" alt="Снимок экрана 2025-09-11 в 21 06 17" src="https://github.com/user-attachments/assets/f10e1758-31d2-406b-8070-2ebdc7e2d6ac" />


In addition to the "!tip" command, there are also "!q" and "!exit" commands that will take you from the game to the terminal. There is also a "!giveup" command that allows the guesser to give up and causes the setter to win.

## Installation and Build
> [!WARNING]
> The installation is temporarily unavailable. You can compile the program yourself using the instructions below.

### Install
Еemporarily unavailable -_-

### Build
> [!WARNING]
> Build requires git, Python 3.7+ with default modules: sys, os, random and pyinstaller.

```bash
git clone https://github.com/0netervezer0/Wordifyery/
cd Wordifyery/main
pyinstaller --onefile main.py
```
