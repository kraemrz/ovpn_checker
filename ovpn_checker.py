from bs4 import BeautifulSoup
import requests
import webbrowser
import subprocess
from time import sleep


html_text = requests.get('https://ovpn.com/sv').text
soup = BeautifulSoup(html_text, 'lxml')
print("Connecting to OVPN.se to check status")

status = soup.find('div', class_="connection-wrapper")

new = (str(status).split(" "))
while ':connected="0"' in new:
    print("Not connected")
    print("Connecting to OVPN")
    subprocess.call([r'PATH_TO_OVPN_APP'])
    sleep(5)

webbrowser.open("https://duckduckgo.com/")
