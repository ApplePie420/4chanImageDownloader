import urllib.request as urllib2
import re
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
location = ""

if(os.path.isdir("4chanImages") == False):
    os.mkdir("4chanImages")
    print("First run, creating folder [4chanImages]")
    location += "4chanImages/"
else:
    location += "4chanImages/"
    
print("Welcome to 4chan image puller")
site = input("Paste thread URL: ")
siteP = site[23:]

board = siteP[1:]
end = board.find("/")
board = board[:end]

if(os.path.isdir(location + board) == False):
    os.mkdir(location + board)
    location += board + "/"
else:
    location += board + "/"

thread = siteP[6:]
end = thread.find("/")
thread = thread[end+1:]

location += thread

if(os.path.isdir(location) == False):
    os.mkdir(location)
    print("New thread, creating folder {}".format(str(thread)))
else:
    location = location

location = location + "/"

print("Board URL: " + siteP)
print("Saving location: " + location)

req = urllib2.Request(url=site, headers=headers)
         
with urllib2.urlopen(req) as response:
    html_response = response.read()
    encoding = response.headers.get_content_charset("utf-8")
    decoded_html = html_response.decode(encoding)

find_word = re.finditer("<img", decoded_html)

counter = 0

for match in find_word:
    url = decoded_html[match.start():]
    end = url.find('src')
    url = url[end:]
    end = url.find('>')
    url = url[:end]
    url = url[5:]
    end = url.find('"')
    url = url[:end]
    url = url[2:]
    if(url[0] == "s"):
        continue 
    url = "https://" + url
    end = url.find(".jpg")
    newURL = url[:end-1] + ".jpg"
    newURL = newURL[20:]
    end = newURL.find("/")
    shortURL = newURL[end+1:]
    fileLocation = location + shortURL
    if(os.path.exists(fileLocation)):
        print("Skipping {} (file already exists)".format(shortURL))
        counter += 1
        continue
    else:
        try:
            urllib2.urlretrieve(url, fileLocation)
            print("Downloaded file {}".format(shortURL))
        except:
            print("File {} not found, skipping...".format(shortURL))
            continue
    counter += 1
