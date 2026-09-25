db = {}
with open('index.md', 'r') as data:
    for line in data.readlines():
        if line.startswith('<!---') and line.strip().endswith('--->'):
            label = line[6:line.find(' --->')]
            if label in db:
                db[label] += 1
            else:
                db[label] = 1

print(db)
                         
