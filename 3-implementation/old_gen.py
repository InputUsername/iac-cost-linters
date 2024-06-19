import csv
import webbrowser

with open('../2-pattern-extraction/pattern_occurrences.csv', 'r') as f:
    r = csv.DictReader(f)
    old_gen = [row['url'] for row in r if row['pattern'] == 'Old generation']

n = len(old_gen)
for i, url in enumerate(old_gen):
    print(f'{i+1}/{n}', url)
    webbrowser.open(url)
    input()
