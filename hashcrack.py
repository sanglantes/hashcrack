import argparse
import codecs
from hashlib import *
parser = argparse.ArgumentParser(description=f'''HashCrack is a Python-based hash cracker with support for salts.
Available hash functions are: {'MD5, MD4, MD5-SHA1, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHA512_224, SHA512_256, SHAKE_128, SHAKE_256, BLAKE2B, BLAKE2S, RIPEMD160, WHIRLPOOL, SM3, MDC2'.lower()}''')
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
        print(f'{unparsed[i]} {digest}')
        i = i + 1
        if attack_hash == digest:
            print(f'\033[1;32;40mCRACKED! {attack_hash} is {unparsed[i - 1]}')
            break
