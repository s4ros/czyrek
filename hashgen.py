###############################################################################
#
# ██   ██  █████  ███████ ██   ██  ██████  ███████ ███    ██
# ██   ██ ██   ██ ██      ██   ██ ██       ██      ████   ██
# ███████ ███████ ███████ ███████ ██   ███ █████   ██ ██  ██
# ██   ██ ██   ██      ██ ██   ██ ██    ██ ██      ██  ██ ██
# ██   ██ ██   ██ ███████ ██   ██  ██████  ███████ ██   ████
# SHA1 hash generator for testing purposes
#           (c) 201 by s4ros
#               www.s4ros.it
import hashlib
import sys

def generateSHA1(text):
    sha_1 = hashlib.sha1()
    sha_1.update(text.encode("utf-8"))
    print(sha_1.hexdigest())

if __name__ == "__main__":
    generateSHA1(sys.argv[1])
