import pickle
from pprint import pprint
from lib.data_preparation import read_and_generate_dataset

all_data = read_and_generate_dataset(
    "data/PEMS08/pems08.npz",
    1,
    1,
    3,
    12,
    12,
    True
)

print("=== extracted data; saving to pickle ===")
with open("data.bin", "wb") as f:
    pickle.dump(all_data, f)
print("=== done ===")