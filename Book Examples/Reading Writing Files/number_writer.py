from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')

def write_json_file():
        contents = json.dumps(numbers)
        path.write_text(contents)
        print('File written.')

def read_json_file():
        contents = path.read_text()
        numbers = json.loads(contents)
        print('Contents of file:')
        print(numbers)


write_json_file()
read_json_file()

print(path.read_text())
