import os
import uuid


class DonkeyDB:
    def __init__(self):
        self._db_file = os.fdopen(os.open("donkey.db", os.O_RDWR | os.O_CREAT), "rb+")
        self._keys_file = os.fdopen(os.open("donkey.keys", os.O_RDWR | os.O_CREAT), "r+")
        self._keys = {}

        for line in self._keys_file:
            key, offset, length = line.split(",")
            self._keys[key] = {"offset": int(offset), "length": int(length.strip())}

    def _generate_key(self):
        return str(uuid.uuid4())

    def insert(self, data):
        key = self._generate_key()
        bytes = data.encode("utf-8")
        bytes_length = len(bytes)

        self._db_file.seek(0, 2)
        offset = self._db_file.tell()
        self._db_file.write(bytes)

        self._keys[key] = {"offset": offset, "length": bytes_length}
        self._keys_file.seek(0, 2)
        self._keys_file.write(f"{key},{offset},{bytes_length}\n")

        return key

    def update(self, key, data):
        pass

    def get(self, key):
        offset = self._keys[key]["offset"]
        length = self._keys[key]["length"]

        self._db_file.seek(offset)
        return self._db_file.read(length).decode("utf-8")

    def delete(self, key):
        pass


if __name__ == "__main__":
    db = DonkeyDB()

    key = db.insert("hello world!")
    print(db.get(key))
