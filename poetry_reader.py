import json

with open('fixture.ndjson') as f:
# with open('gutenberg-poetry-v001.ndjson') as f:
    lines = f.read()

lines = lines.split('\n')
lines.pop()

x = [json.loads(line)['s'] for line in lines]

# with open("poetry_corpus.txt", "w") as outfile:
    # outfile.write("\n".join(x))
