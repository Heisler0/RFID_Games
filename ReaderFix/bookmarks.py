import webbrowser
from keyboard_alike import reader

reader = reader.Reader(0xffff, 0x0035, 8, 8, should_reset=True)

reader.initialize()

websites = {
            '09359668' : 'http://www.google.com/'
            }

while True:

    bookmark = ""
    while bookmark not in websites:
        bookmark = reader.read_card()

    url = websites[bookmark]

    webbrowser.open(url)

    print("Opening " + url)
