import sys
import hashlib as hash

mode = sys.argv[1]
run = sys.argv[2]
encoded = str.encode(run)
byted = bytes(encoded)
hashed = hash.md5(byted)
digested = hashed.hexdigest()

print(digested)

file = open('hash.txt', mode)
file.write(digested + '\n')
file.close()
