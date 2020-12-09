import argparse
import json
import os
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_path', type=str, help='Path to access.log file')
parser.add_argument('--result_file', dest='result_path', type=str, help='Path to result file', default=None)
args = parser.parse_args()

path = os.path.abspath(args.file_path)

type_stat = defaultdict(int)
with open(path, 'r') as file:
    for line in file:
        type_stat[line.split(' ')[5]] += 1

if args.result_path is None:
    result_path = os.path.join(os.path.curdir, 'script_result.txt')
else:
    result_path = os.path.abspath(args.result_path)

with open(result_path, 'w') as file:
    if result_path.endswith('.json'):
        json.dump(type_stat, file, indent=4)
    else:
        output = ''
        for key, value in type_stat.items():
            output += key + ' ' + str(value) + '\n'
        file.write(output)
