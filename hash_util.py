import hashlib as hl
import json

#name with underScore
#it doesn't need export or other things and
#we just import it to other place with import name of file 

def hash_string_256(string):
    return hl.sha256(string).hexdigest()

# def hash_block(block):
#     # hashed_block="-".join([str(value) for key,value in block.items()])
#     # return hashed_block
#     # return hashlib.sha256(json.dumps(block).encode()).hexdigest()
#     return hl.sha256(json.dumps(block,sort_keys=True).encode()).hexdigest()
def hash_block(block):
    # hashed_block="-".join([str(value) for key,value in block.items()])
    # return hashed_block
    # return hashlib.sha256(json.dumps(block).encode()).hexdigest()
    return hash_string_256(json.dumps(block,sort_keys=True).encode())