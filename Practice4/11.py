import json

source = json.loads(input())
patch_obj = json.loads(input())

def apply(source, patch):
    for key, val in patch.items(): 
        if val is None:
        #{"a":5,"b":3}
        #{"a":None}
            source.pop(key, None)
            #{"b":3}
        elif key not in source:
        #{"a":4}
        #{"b":5}
            source[key] = val
            #{"a":4,"b":5}
        elif isinstance(val, dict) and isinstance(source.get(key), dict):
            apply(source[key], val)
        else:
            source[key] = val
apply(source, patch_obj)
print(json.dumps(source, separators=(',', ":"), sort_keys=True))