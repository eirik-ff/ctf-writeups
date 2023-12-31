
wal = open("inventory.db-wal", "rb").read()

for chunk in wal.split(b"\x04\x55")[1:]:
    block_size = chunk[0]
    int_size = chunk[1]
    uuid = chunk[2:38].decode()
    name = chunk[38:-4 - int_size].decode()
    quantity_bytes = chunk[-4 - int_size:-4]

    print("int size", int_size, uuid, name, int.from_bytes(quantity_bytes, "big"))

