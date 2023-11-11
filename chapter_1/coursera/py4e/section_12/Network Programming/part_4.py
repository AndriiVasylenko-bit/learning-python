import socket



print(ord('H'))
print(ord('e'))
print(ord('\n'))

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

# Python String to Bytes
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    mystring = data.decode()
    print(data)
    print(mystring)
mysock.close()