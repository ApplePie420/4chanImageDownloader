# 4chan Image Downloader
Have you ever found an interesting thread on 4chan with lots of cool images (memes, nudes, etc) that you wanted to download, but you´re lazy f*** and don´t want to click like a monkey? Well then, fear not to use my image downloader! Simply paste in URL and you´ll get well-organized file structure with ALL files from thread (except bugs, see Issues)

And you know what´s best?
__WE SUPPORT EVERY 4CHAN FILE FORMAT!__

Including:
- jpg
- png
- webm
- gif

# How to use
You need [Python](https://www.python.org/downloads/) installed
Just download latest version for your OS (be sure to use python 3!), install and you are ready to go!

## Interacting with console
Just as you are lazy downloading all those images, i´am lazy creating nice-looking UI for this program. My excuse is, that only "controller" in this program is one input with URL and you really dont need fancy UI for that. 

So after you installed Python, double-click _imageParser.py_ (name WIP), and you´ll be greeted by start screen which prompts you to enter URL. Copy and paste __FULL URL__ of the 4chan site (like: "http://boards.4chan.org/b/thread/783940220", without quotes) and press _enter_.

After hitting enter, console will spit some info on you, you can ignore that if you want to. It will tell you where files are saved, what board you are downloading from etc. Oh, also current progress. Program will try to download all available images.

You should get folder called _4chanImages_ in folder where *.py file is located, and that file should contain subfolders with names by boards you downloaded from (e.g. "b", "pol" etc). Those folder will contain more subfolders, each with thread number (like "783940220") and this final folder will contain all dem sweet imgaes.

![puller](https://preview.ibb.co/hfQGsf/imagepuller.png)

# Known Issues
- Code is awfully bodged so sometimes it creates unnecessary folders or put stuff outside folders. If this happens, open new issue and write : full URL of thread (mainly with thread number and board) and what happened (where were files put etc))
- Few boards will cause Error 403, but not in regular intervals (maybe request error?)

### Few disclaimers and stuff
For god´s sake, your own sanity and life of innocent people, please __DONT__ look at the source code. It´s bodged sh!t together, i made it in few hours while i was bored, and i´am not planning to expand it, beautify or do anything with it (unless 4chan changes its storaging strategy and whole thing wont work).

This thing was developed as tool for personal use, thus it doesn´t look like a product neither visually nor by code. 

I also don´t take any responsibilieties for copyright stuff. All images are stored on 4chan.org and belongs to them, this software just download publicly available link to that image. If any problems, contact 4chan.

You can also support this project (which will motivate me to add new features and maybe build an UI) by sending few ETH coins to: 
`0xe972B42e37E1Be9837851788B527014662F9AF0869`
