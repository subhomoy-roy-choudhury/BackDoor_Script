import hashlib
import os
import base64
import subprocess
import sys

print(sys.argv)

BUF_SIZE = 65536

md5 = hashlib.md5()
sha1 = hashlib.sha1()

a = 'test.py'

with open(a, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
output = subprocess.check_output(f"base64 {a}", shell=True)

print(output)
# print(base64.b64decode(output).decode('utf-8'))
exec(base64.b64decode(output).decode('utf-8'))


if __name__ == '__main__':

    import argparse
    
    parser = argparse.ArgumentParser(description="Simple File Encryptor Script")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()


