from hashlib import sha256
h = sha256()
h.update(b'python')
hash = h.hexdigest()
print(hash)
