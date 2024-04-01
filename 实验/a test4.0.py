from pathlib import Path
import json

num=[1,2,3]
path=Path('a try.json')
content=json.dumps(num)
path.write_text(content)
