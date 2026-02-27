import json
import re
import sys

def resolve_query(data, query):
    pattern = re.compile(r'\.?([a-zA-Z_][a-zA-Z0-9_]*)|\[([0-9]+)\]')
    current = data
    for match in pattern.finditer(query):
        key, index = match.groups()
        if key:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return "NOT_FOUND"
        elif index:
            if isinstance(current, list):
                idx = int(index)
                if 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return "NOT_FOUND"
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(',', ':'))


json_str = sys.stdin.readline().strip()
data = json.loads(json_str)

q = int(sys.stdin.readline())
for _ in range(q):
    query = sys.stdin.readline().strip()
    print(resolve_query(data, query))