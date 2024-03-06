from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')

p.read_text()