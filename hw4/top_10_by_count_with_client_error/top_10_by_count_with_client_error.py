import argparse
import json
import os
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_path', type=str, help='Path to access.log file')
parser.add_argument('--result_file', dest='result_path', type=str, help='Path to result file', default=None)
args = parser.parse_args()

path = os.path.abspath(args.file_path)

stat = defaultdict(int)
with open(path, 'r') as file:
    for line in file:
        line_elements = line.split(' ')
        if line_elements[8].startswith('4'):
            ip_url_status = (line_elements[0], line_elements[6], line_elements[8])
            ip_url_status = ' '.join(ip_url_status)
            stat[ip_url_status] += 1

stat = sorted(stat.items(), key=lambda v: v[1], reverse=True)[:10]

if args.result_path is None:
    result_path = os.path.join(os.path.curdir, 'script_result.txt')
else:
    result_path = os.path.abspath(args.result_path)


with open(result_path, 'w') as file:
    if result_path.endswith('.json'):
        output = [{'ip': item[0].split(' ')[0],
                   'url': item[0].split(' ')[1],
                   'status_code': item[0].split(' ')[2],
                   'count': str(item[1])} for item in stat]
        json.dump(output, file, indent=4)
    else:
        output = ''
        for item in stat:
            output += item[0] + ' ' + str(item[1]) + '\n'
        file.write(output)