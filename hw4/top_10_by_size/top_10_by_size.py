import argparse
import json
import os
from collections import defaultdict, OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_path', type=str, help='Path to access.log file')
parser.add_argument('--result_file', dest='result_path', type=str, help='Path to result file', default=None)
args = parser.parse_args()

path = os.path.abspath(args.file_path)

with open(path, 'r') as file:
    size = OrderedDict()
    count = defaultdict(int)
    for line in file:
        line_elements = line.split(' ')
        url_status_size = (line_elements[6], line_elements[8], line_elements[9])
        url_status_size = ' '.join(url_status_size)
        try:
            size[url_status_size] = int(line_elements[9])
        except ValueError:
            continue
        count[url_status_size] += 1

size = sorted(size.items(), key=lambda v: v[1], reverse=True)[:10]
for item in size:
    print(item[0], count[item[0]])

if args.result_path is None:
    result_path = os.path.join(os.path.curdir, 'script_result.txt')
else:
    result_path = os.path.abspath(args.result_path)

with open(result_path, 'w') as file:
    if result_path.endswith('.json'):
        output = [{'url': item[0].split(' ')[0],
                   'status_code': item[0].split(' ')[1],
                   'size': item[0].split(' ')[2],
                   'count': str(count[item[0]])} for item in size]
        json.dump(output, file, indent=4)
    else:
        output = ''
        for item in size:
            output += item[0] + ' ' + str(count[item[0]]) + '\n'
        file.write(output)
