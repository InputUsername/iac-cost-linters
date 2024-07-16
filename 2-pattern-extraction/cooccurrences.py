import csv

with open('pattern_occurrences.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    occurrences = list(reader)

rows = []

for pattern, url in occurrences:
    _, _, _, owner, repo, _, commit = url.split('/')

    rows.append({
        'repo': f'{owner}/{repo}',
        'commit': commit,
        'pattern': pattern,
    })

rows = sorted(rows, key=lambda r: r['repo'])

with open('cooccurrences_with_commits.csv', 'w') as f:
    writer = csv.DictWriter(f, ['repo', 'commit', 'pattern'])
    writer.writeheader()
    writer.writerows(rows)
