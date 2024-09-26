import hashlib
import sys

pswd=sys.argv[0]
dict=sys.argv[1]


with open(pswd, 'r') as file:
    pswd=file.read()


with open(dict, 'r') as file:
    dict=file.read()
    
def reversible_hash(data):
    hash_object=hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def reverse_hash(hash_value):
    for i in range(1000000):
        test_data=str(i)
        if reversible_hash(test_data)==hash_value:
            return test_data
    return None

hashed_data=reversible_hash(pswd)
recovered_data=reverse_hash(hashed_data)

print("Original Data: "+ pswd)
print("Hashed Data: "+ hashed_data)
print("Recovered Data: "+ recovered_data)

