import argparse
from sty import bg
from hashlib import *

print('''
██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
███████║███████║╚█████╗░███████║██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝''')
parser = argparse.ArgumentParser(description=f'''HashCrack is a Python-based hash cracker with support for salts.
Available hash functions are: {'MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, BLAKE2B, BLAKE2S'.lower()}''')
parser.add_argument('-H', nargs='?', metavar='hash', required=True, dest='hash', help='string to be cracked')
parser.add_argument('-s', nargs='?', metavar='salt', required=False, dest='salt', help='salt')
parser.add_argument('-t', nargs='?', metavar='function', required=True, dest='function', help='hash function')
parser.add_argument('-l', nargs='?', metavar='dictionary', required=True, dest='dictionary', help='dictionary file')
args = parser.parse_args()
attack_hash = args.hash
hash_type = eval(args.function)
if args.salt:
    salt = bytes(args.salt.encode('utf-8'))
dictionary = args.dictionary

f = open(f'{dictionary}', 'r')
unparsed = f.read()
unparsed = unparsed.replace('\n', ' ').split(' ')
f.close()
i = 0
with open(f'{dictionary}', 'rb') as f:
    for line in f.readlines():
        pw = line.strip()
        if not args.salt:
            salt = b''
        digest = hash_type(pw+salt).hexdigest()
        print(f'{unparsed[i]}: {digest}')
        i = i + 1
        if attack_hash == digest:
            print(f'{bg.green}CRACKED! {attack_hash} is {unparsed[i - 1]}{bg.green}')
            print(f'{bg.black}')
            break
if not attack_hash == digest:
    print(f'{bg.red}Could not crack the hash.{bg.red}')
    print(f'{bg.black}')
