## Downloading image form internate


import requests

img_url = "https://goo.gl/JxktPw"
r = requests.get(img_url)

with open("pybook.png", "wb") as f:
    f.write(r.content)


## Saving webpage


# import requests
# import os
# import webbrowser as web
# url = "http://dimikcomputing.com"
# response = requests.get(url)
#
# with open("dimik.html", "w", encoding=response.encoding) as f:
#     f.write(response.text)
#
# file_path = os.path.realpath("dimik.html")
# print(file_path)
# web.open("file://" + file_path)