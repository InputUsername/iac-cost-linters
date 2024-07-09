import json

with open('final.json', 'r') as f:
    data = json.load(f)

for a in data:
    s = set(a['codes'])
    if 'unrelated' not in s and 'test' not in s and 'alert' not in s:
        print(a['url'])
        a['codes'].append('change')

with open('final2.json', 'w') as f:
    json.dump(data, f)
