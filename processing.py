import os
import json
import webbrowser

with open('diffs.json', 'r') as diffs_file:
    diffs: list[dict[str]] = json.load(diffs_file)

# for item in diffs:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     url = item['url']
#     print(f'========== {url} ==========')
#     print('existing codes:', item['existing_codes'])

#     for file in item['files']:
#         name = file['filename']
#         diff = file['patch']
#         print(f'----------\n{name}\n----------\n{diff}')

#     input()

for d in diffs:
    if 'saving' not in d['existing_codes'] or len(d['codes']) != 0:
        continue

    print(d['url'])
    webbrowser.open(d['url'])
    input()
