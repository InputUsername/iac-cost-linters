import json

from nltk.metrics import masi_distance
from nltk.metrics.agreement import AnnotationTask


with open('abel2.json', 'r') as f1, open('koen2.json', 'r') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

assert len(data1) == len(data2)

data = []
for (a, b) in zip(data1, data2):
    assert a['url'] == b['url']

    data.append((0, a['url'], frozenset(a['codes'])))
    data.append((1, a['url'], frozenset(b['codes'])))

task = AnnotationTask(distance=masi_distance)
task.load_array(data)

alpha = task.alpha()

print(f'alpha={alpha:.6f}')
