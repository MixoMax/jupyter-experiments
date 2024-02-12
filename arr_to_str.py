import random
import sqlite3
from tqdm import tqdm

def float_to_char(val: float) -> str:
    if val > 1.0 or val < -1.0:
        raise ValueError("Value must be between -1.0 and 1.0")
    
    # remap from [-1.0, 1.0] to [0, 255]
    val = int((val + 1) * 127.5)
    return chr(val)

def char_to_float(val: str) -> float:
    # remap from [0, 255] to [-1.0, 1.0]
    return (ord(val) / 127.5) - 1

def arr_to_str(arr: list[float]) -> str:
    out_str = ""
    for val in arr:
        out_str += float_to_char(val)
    return out_str

def str_to_arr(in_str: str) -> list[float]:
    out_arr = []
    for val in in_str:
        out_arr.append(char_to_float(val))
    return out_arr



db = sqlite3.connect("test.db")

cursor = db.cursor()

cmd = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, data TEXT)"

cursor.execute(cmd)


# insert some data

for _ in tqdm(range(100_000)):
    data = [random.uniform(-1, 1) for _ in range(1024)]
    cursor.execute("INSERT INTO test (data) VALUES (?)", (arr_to_str(data),))
db.commit()