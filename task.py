def create_keys(start, end):
    mnemo = Mnemonic("english")
    keys = []
    for _ in range(start, end):
        mnemonic = mnemo.generate(256)
        wif_key, compressed_address, private_key, seed, master_public_key = create_key_from_mnemonic(mnemonic)
        keys.append((mnemonic, wif_key, compressed_address, private_key, seed, master_public_key))
    return keys
