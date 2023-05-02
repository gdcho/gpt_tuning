import csv
import json

input_csv = 'genre_data.csv'
output_json = 'prompt_completion_pairs.json'

def read_csv_data(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def create_prompt_completion_pairs(data):
    pairs = []
    for row in data:
        prompt = f"Write a {row['genre']} book summary based on this information: {row['summary']}"
        completion = row['summary']
        pairs.append({"prompt": prompt, "completion": completion})
    return pairs

def write_json_data(file_path, data):
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

if __name__ == "__main__":
    csv_data = read_csv_data(genre_data.csv)
    prompt_completion_pairs = create_prompt_completion_pairs(csv_data)
    write_json_data(output_json, prompt_completion_pairs)
