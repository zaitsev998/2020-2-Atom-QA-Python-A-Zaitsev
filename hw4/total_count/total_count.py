import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_path', type=str, help='Path to access.log file')
parser.add_argument('--result_file', dest='result_path', type=str, help='Path to result file', default=None)
args = parser.parse_args()

path = os.path.abspath(args.file_path)

with open(path, 'r') as file:
    count = 0
    for line in file:
        count += 1

if args.result_path is None:
    result_path = os.path.join(os.path.curdir, 'script_result.txt')
else:
    result_path = os.path.abspath(args.result_path)

with open(result_path, 'w') as file:
    if result_path.endswith('.json'):
        output = {'requests count': count}
        json.dump(output, file, indent=4)
    else:
        output = f'requests count {count}'
        file.write(output)