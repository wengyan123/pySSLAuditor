addr = "www:334"


if addr.find(':') == -1:
    hostname = addr
    port = 443
else:
    hostname, port = addr.split(':')

print(hostname)
print(port)