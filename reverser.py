import csv
from pathlib import Path
import sys

INPUT_FOLDER = Path("input csv")
OUTPUT_FOLDER = Path("output csv")

if not INPUT_FOLDER.exists():
    print(f"Error: Input folder '{INPUT_FOLDER}' was not exist")
    INPUT_FOLDER.mkdir(exist_ok=True)
    sys.exit(1)

OUTPUT_FOLDER.mkdir(exist_ok=True)

try:
    input_csv = next(INPUT_FOLDER.glob("*.csv"))
except StopIteration:
    print(f"Error: No CSV files found in '{INPUT_FOLDER}'")
    sys.exit(1)

output_csv = OUTPUT_FOLDER / (input_csv.stem + "_reversed.csv")

with open(input_csv, "r", encoding="utf-8", newline='') as f:
    reader = list(csv.reader(f))
    header = reader[0]
    data = reader[1:]

# Find the index of the Playlist name column
playlist_idx = header.index("Playlist name")

# Create new playlists 
for row in data:
    row[playlist_idx] = f"{row[playlist_idx]}-reversed"

with open(output_csv, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(reversed(data)) # save as reversed

print(f"Reversed CSV saved as '{output_csv}'")