import re
import urllib.request

# Open the file you want to get your URLs from
file = open('file', "r")

# You have to add your own regex in the findall() function (I knew what I was looking for myself and made a regex for that
# not sure if this actually works with any given regex and file, as I made this for myself as a one time thing.)
for line in file:
    text = file.read()
    urls = re.findall(' regex here ', text)
    print(urls) # Shows the 'random' part of the url, this is what I was looking for myself

# Checks for information so that the final list contains only working URLs
newURLS = []
for url in urls:
    if "." in url:
        if url not in newURLS:
            newURLS.append(url)

# Writes the final list of (hopefully) working URLs to a "URLs.txt" file. Each line will contain one URL and newline.
with open("URLs.txt", "w") as urlEnds:
    for url in newURLS:
        # Might give you only the 'random' end part for the url (Didn't test for that)
        urlEnds.write(url + "\n")

# Goes through every URL, downloads the image and names it "image_i.png".
with open("URLs.txt", "r") as allUrls:
    # You could just add a function that counts the lines in the URL file and use that in range()
    for i in range(5):
        filename = "image_" + str(i) + ".png"
        image_url = allUrls.readline()
        urllib.request.urlretrieve(image_url, filename)
        print(str(i+1) + " images downloaded...")
