#! python
# find_and_open_url.py - this script will try to:
# 1) find url addresses from the command line - if the command line is empty, it will search the clipboard for
#the text
# 2 - in a moment it will open all these urls onto your website in the different carts
# X 2020 Arnold Cytrowski

import sys, pyperclip, webbrowser, re

def search_for_urls(text: str):
    urls = []
    url_reg = re.compile(r'(http|https)://\S+')

    for match in url_reg.finditer(text):
        urls.append(match.group())

    for url in urls:
        webbrowser.open(url)

# if len(sys.argv) > 1:
#     text = ' '.join(sys.argv[1:])
# else:
#     text = pyperclip.paste()

search_for_urls('https://onet.pl to dobrze ze http://wp.pl')



