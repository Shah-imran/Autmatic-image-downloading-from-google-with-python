from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

import os

fileList = os.listdir("2K")

print(fileList)

for i in fileList:
    with open("2K/"+i, "r", encoding="utf-8") as f:
        names = f.read()

    names = names.replace("\n", ",")
    print("Running File - " + i)
    arguments = {"keywords":names,"limit":200,"print_urls":False, "chromedriver":"chromedriver.exe"}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)

    print("Finished - " + i)