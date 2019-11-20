import hashlib
passwd = "123"
salt = "#0789"
hash = hashlib.md5(salt.encode())
hash.update(passwd.encode())
res = hash.hexdigest()
print(type(res))