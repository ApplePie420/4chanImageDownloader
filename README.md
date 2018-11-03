# 4chan Image Downloader
Have you ever found an interesting thread on 4chan with lots of cool images (memes, nudes, etc) that you wanted to download, but you´re lazy f*** and don´t want to click like a monkey? Well then, fear not to use my image downloader! Simply paste in URL and you´ll get well-organized file structure with ALL files from thread (except bugs, see Issues)

# How to use
You need [Python](https://www.python.org/downloads/) installed
Just download latest version for your OS (be sure to use python 3!), install and you are ready to go!

## Interacting with console
Just as you are lazy downloading all those images, i´am lazy creating nice-looking UI for this program. My excuse is, that only "controller" in this program is one input with URL and you really dont need fancy UI for that. 

So after you installed Python, double-click _imageParser.py_ (name WIP), and you´ll be greeted by start screen which prompts you to enter URL. Copy and paste __FULL URL__ of the 4chan site (like: "http://boards.4chan.org/b/thread/783940220", without quotes) and press _enter_.

After hitting enter, console will spit some info on you, you can ignore that if you want to. It will tell you where files are saved, what board you are downloading from etc. Oh, also current progress. Program will try to download all available images, but sometimes for some reason (maybe 4chan´s storage optimalization) some files are moved right after posting and my program cannot find them, so you have to download them manually (just copy the image number and search it in browser).

You should get folder called _4chanImages_ in folder where *.py file is located, and that file should contain subfolders with names by boards you downloaded from (e.g. "b", "pol" etc). Those folder will contain more subfolders, each with thread number (like "783940220") and this final folder will contain all dem sweet imgaes.

# Known Issues
- Sometimes a file on server cannot be found, i have no clue if its bug in my program or some sort of 4chan´s storage optimalization. 
- Code is awfully bodged so sometimes it creates unnecessary folders or put stuff outside folders. If this happens, open new issue and write : full URL of thread (mainly with thread number and board) and what happened (where were files put etc))
- Few boards will cause Error 403, but not in regular intervals (maybe request error?)
