def insert_keys(keys):
    try:
        conn = cnxpool.get_connection()
        cursor = conn.cursor(prepared=True)
        table_name = f"keys_v3{current_process().pid}"
        history_table_name = f"keys_history_v3{current_process().pid}"
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (mnemonic TEXT, wif_key TEXT, compressed_address TEXT, private_key TEXT, seed TEXT, master_public_key TEXT)")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {history_table_name} (child_key TEXT, history TEXT)")
        insert_query = f"INSERT INTO {table_name} (mnemonic, wif_key, compressed_address, private_key, seed, master_public_key) VALUES (%s, %s, %s, %s, %s, %s)"
        history_query = f"INSERT INTO {history_table_name} (child_key, history) VALUES (%s, %s)"
        index = create_index(keys)  # Create an index for the generated keys
        for key in keys:
            mnemonic, wif_key, compressed_address, private_key, seed, master_public_key = key
            cursor.execute(insert_query, (mnemonic, wif_key, compressed_address, private_key, seed, master_public_key))
            child_keys = create_child_keys(master_public_key)  # Create child keys using different derivation paths
            for child_key in child_keys:
                if search_key(child_key):  # Search for the child key in the index
                    history = check_key_history(child_key)  # Check the history of the child key
                    if history:
                        cursor.execute(history_query, (child_key, history))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
