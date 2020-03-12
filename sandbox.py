import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

block = {
"chain": [
{
"index": 1,
"previous_hash": 1,
"proof": 100,
"timestamp": 1583959884.3455267,
"transactions": []
}
],
"length": 1
}



string_block = json.dumps(block, sort_keys=True) + "5"

check_hash = hashlib.sha256(string_block.encode())


print(block)
print(string_block)
print(check_hash.hexdigest())