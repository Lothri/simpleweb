# import socket
#
import urllib.request
from bs4 import BeautifulSoup

url = "https://boilerplate-project-exercisetracker.lothri.repl.co"

fhand = urllib.request.urlopen(url)

 for line in fhand:
     if (line.decode().startswith("a") is True):
         print(line)

the_whole_thing = fhand.read()

soup = BeautifulSoup(the_whole_thing, 'html.parser')
print(soup('input'))

fhand.close()


#### OR
#
# new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# new_sock.connect((url, 80))
# cmd = "GET https://boilerplate-project-exercisetracker.lothri.repl.co HTTP/1.1\n\n".encode()
# new_sock.send(cmd)
#
# while True:
#     data = new_sock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode())
# new_sock.close()
#

