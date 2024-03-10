# Short program to fomat any json file to be readable

from pathlib import Path
import json


def get_path():
    while True:
        json_path = Path(input('Enter absolute windows path: '))
        if not json_path.is_absolute():
            print('Path must be an absolute path.')
        return json_path

json_path = get_path()
try:
    json_contents = json.loads(json_path.read_text())
    json_path.write_text(json.dumps(json_contents, indent = 2))
    print('JSON file formated.')
except Exception as exception:
    print(exception)


