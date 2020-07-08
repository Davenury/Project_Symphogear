# Project_Symphogear
![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue) ![version](https://img.shields.io/badge/version-0.0.0-blue) 
![files](https://img.shields.io/badge/Files-Included-brightgreen) ![contributors](https://img.shields.io/badge/Contributors-1.5-brightgreen)

***

## Table of Contents
* [Latest changes](latest-changes)
* [Contributors](#contributors)
* [Technologies](#technologies)
* [Instalation](#instalation)
* [What is ready for now?](#what-is-ready-for-now)
* [Source Files](#source-files)
* [Why?](#why)
* [Goal](#goal)
* [Inspiration](#inspiration)
* [To Do Before Play](#to-do-before-play)
* [Main Quest](#main-quest)
* [How To Help?](#how-to-help)

***

## Latest Changes
Below I'll put a list with all major updates that have been uploaded to this repo with dates:
 * (08.07.2020):
   * Music Player runs and it's awesome! (if I could say that)

***

## Contributors

Right now, I'm all alone with writing the code, but I have my friend, who who tests it. So... it's like the two of us, but one doesn't code, so... 1.5? Will it be?

***

## Technologies

Technologies used in this "little" project:
* Python
* Pygame
* Unit tests library for Python (just for tests)

***

## Instalation
Before you start installation of this game, be sure, that you have installed Python (most preferably version 3). If you don't know how to check, if you already have python (you could have and don't even know about it), then:
* Open command line (type cmd in your search bar) and type:
```
python --version
```
* If the response looks something like 

![Python version](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/python_version.png)

then you have Python and you don't have to install it.
* If the response it something simillar to "python is not known command", you don't have python and need to install it.

Don't know how to install it? Check out this page [Install Python](https://realpython.com/installing-python/)

### Instalation for these ones, who don't know how to git
To install this game, download this reopsitory (see the image below, if you don't know how).
![Download Repository](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/Download_Repository.png)

Then you need to extract it (I think that's obvious enough) and go to the Next Step in Instalation. I would also highly recommend you to learn the basics of git (init, clone, pull), because it will be easier for you in the future.

### Instalation for these ones, who would like to know how to git
Git isn't too hard to get to know. The only thing that you'll need is configuration of your git and `git pull` (of course unless you would like to contribute to this project, then you'll need to learn some more of git). If you won't understand any of these points, feel free to either ask me in the mail (dawid199960@gmail.com) or my Facebook / Instagram, whatever. You can also learn the basics of git from 10-minutes movies on YouTube or something like this. Anyway, let's get started:
 * Create account on Github (you'll need to set a password and give them your email).
 * Install git for windows from [this site](https://gitforwindows.org/).
 * Open git bash.
 * Config your git with your username with `git config --global user.name "<Your Name>"` (of course change <Your Name> with your name):
  
  ![Git user.name config](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/git_config_1.png)
  
 * Then config your email with `git config --global user.email <Your email>` (of course change <Tour email> with your email).  
  
  ![Git user.email config](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/git_config_2.png)
  
 * Navigate to folder where you want to have this game, using `cd` and `dir` commands. (cd for directory changes and dir to list all of files and directories in current directory). If you want to have it on your D: disc (which I highly recommend), the first change you would like to make is `cd d:` (if this doesn't work, type `cd ../../../d:` which should work just fine).
 * Initialize new repository on your device with command `git init`:
 
 ![Git init](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/git_init.png)
 
 * Add link to this remote (online) repository with command `git remote add origin https://github.com/Davenury/Project_Symphogear.git`. (Nothing will be on output, if everything goes fine):
 
 ![Git remote add](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/git_remote_add.png)
 
 * Last thing to do is typing `git pull origin master`. It will take some time because of quantity of files included in this repository (images, sounds, music). Don't care about everything in the output, even I don't care about it (of course unless there is something on red or yellow, because that's mean a problem!). Your output should look something like:
 
 ![Git pull](https://github.com/Davenury/Project_Symphogear/blob/master/markdown_images/git_pull.png)
 
 * And that's it. Everything is ready and you know basics of git that are used by you here. Of course there is much more to learn with git but now you know what it is at least! You can to to **Next Step in Instalation**.

### Instalation for these ones, who know how to git
Then I think you know what you should do. Create the folder in which you want to have this game. Then make `git init` to initialize empty repository. Add connection to remote repository (at least that's how I understand this) by typing `git remote add origin https://github.com/Davenury/Project_Symphogear.git`. If this doesn't work, you'll have to use SSH protocole. Then, when you'll have everything ready, go to **Next Step in Instalation**.

### Next step in instalation

Go to your command line (at this moment this game is testes on Windows, so I don't really know, how it will behave on Linux, etc.), change your directory (with `cd` command) to **Project_Sympohgear**. With `dir` command make sure, that there is a `requirements.txt` file. If there is (becuase there should be one), type:

```
pip install -r requirements.txt
```

And that should be it. Game is installed and ready to use (well, now it isn't, because, as I wrote earlier, it's only some unrelated classes, so you won't be doing anything with it, but hey! I'm trying hard!).

***

## What is ready for now?

### Music Player

As for this day (01.07.2020) only one thing is ready and it's Music Player (version 1.0.0) with all of the songs of anime series. If you want to know how to use it, check out [Documentation](https://docs.google.com/document/d/1f7OIKPJsSe8bc_GtXJyFHeuxhh2EukJjlxCXOtYWbbM/edit?usp=sharing). (Well, for now, there isn't much about it, but there will be ^^).
#### How to start it?
Go to **Project_Symphogear** folder, then go to **Ready_Products** folder (`cd Ready_Products`). Then type `pgzrun MusicPlayer.py` and it will start!

As for now:
* right arrow plays next song
* left arrow plays previous song
* space pauses / unpauses a song
* e stops a song
* p plays the song (either from a beginning or plays it one more time)
If you want to change a song, you have to do it manually!

***

## Source Files

All of source files (sounds, music and images) come from Symphogear anime and Internet, so I don't have any rights to it (even if some of them are a bit modificated and I hope that the artists won't bit me :wink:). After all it's a simple game and we all should be happy with it :heart_eyes:

***

## Why

First of all it was supposed to be a simple game for me to understand the basics of Python language. Then I told about it to my friend, who thought it was a good idea, so I've worked with it for a bit. And then I understood how messy my code was, so I've started all from the beginning and here I am now. I don't know where it will lead me. It can be just some project that I won't even finish, but I wouldn't want to do it. I've started it and I want to end it for people, who like Symphogear as much as I do. For them to be one more time with characters we've benn watching for 5 seasons.

***

## Goal

My goal is simple: write a good game with some good story line. To write it for fans to be with the characters once again. To write it for people, who never heard about it but (I hope) will want to watch this anime and go through this path with us. Finally, to write it for me, to prove myself, that I can do some good things too.

***

## Inspiration

Inspiration for this little project was an anime called "Senki Zesshou Symphogear", which I want to recommand you to watch, because it's worth your time. It doens't matter if you are 15 or 50 (if you are younger, don't watch it. It isn't very scary, but it has some things, that you shouldn't watch right now. Either you won't understand it or get scared about it, and I will need to apologize. Do I need that? Hell, no!).

***

## To Do Before Play

Main questline of this game (at least I think now) will be set after the final of season 5, so if you don't want to have a bunch of spoliers, first watch the anime. Of course there's something I need to do before you'll be even able to start to think about playing. I need to write it first :hushed: .

***

## Main Quest

For this moment, I'm not quite sure what will be the main questline for this game, but we'll figure something out for sure!

***

## How to help?

If you want to help us with this "little" project, you can do it in two ways:

* If you can code in Python language (or any other language, tbh, because Python is easy enough to learn) and:
  * you have some experience and you're eager
      Write to me (dawid199960@gmail.com) and become a full contributor to this "little" project.
  * you don't have experience, but you are eager
      Also write to me (dawid199960@gmail.com). You can learn some new things and write it in your CV (if you aren't ashamed enough).
      
* If you can't code in any language and don't want to learn it:
  * if you like testing something and think, you'll do it good:
      Test this project and write to me (dawid199960@gmail.com) with all the bugs / mistakes you've found (for example: music isn't playing, game doesn't start, etc.)
      
  * if you like testing, but you aren't sure you'll do it good:
      Don't be scared, we won't eat you alive, because you could mess up something. We're all just humans after all, right?
