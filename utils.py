import base58
import ecdsa
import hashlib

from mnemonic import Mnemonic

def create_key_from_mnemonic(mnemonic):
private_key = hashlib.sha256(seed).digest()
sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
wif_key = base58.b58encode_check(b'\x80' + private_key + b'\x01')
compressed_public_key = b'\x02' + sk.get_verifying_key().to_string()[:32] if
int.from_bytes(sk.get_verifying_key().to_string()[-1:], 'big') % 2 == 0 else b'\x03' +
sk.get_verifying_key().to_string()[:32]
hash160 = hashlib.new('ripemd160')
hash160.update(hashlib.sha256(compressed_public_key).digest())
compressed_address = base58.b58encode_check(b'\x00' + hash160.digest())
return wif_key.decode(), compressed_address.decode(), private_key.hex(), seed.hex()
