import hashlib
import sys

pswd=sys.argv[1]
dict=sys.argv[2]

def reversible_hash(data):
    hash_object=hashlib.sha256(data.encode())
    return hash_object.hexdigest()

with open(pswd, 'r') as file:
    passwords=file.readlines()

with open(dict, 'r') as file:
    words=file.readlines()

for password in passwords:
    password = password.split(':')
    password[1] = password[1].strip()
    for word in words:
        word = word.strip()
        if reversible_hash(word) == password[1]:
            print(password[0] + ':' + word)

