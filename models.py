def main():
    start_time = time.time()

    total_keys = 0
    table_count = 0

    with Pool(processes=num_processes) as pool:
        while total_keys < 30000000:
            tasks = []
            for _ in range(num_processes):
                keys = create_keys(total_keys, total_keys + batch_size)
                tasks.append(keys)
                total_keys += batch_size

            insert_keys(tasks)

            if total_keys % keys_per_table == 0:
                table_count += 1

            if total_keys % 100000 == 0:
                print(f"Inserted {total_keys} keys in {time.time() - start_time:.2f} seconds")

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
