import pkg_resources


def load_file(filename, directory):
    path = '/'.join((directory, filename))
    data = pkg_resources.resource_string(__name__, path)
    data = data.decode('UTF-8', 'replace')
    rows = []
    for line in data.split('\n'):
        if line.startswith('#') or len(line) == 0:
            continue
        s = line.split(', ')
        rows.append(s)
    return rows

def load_weights(filename="ann_weights.csv", directory="data"):
    """Load Neural Network Weights."""
    rows = load_file(filename, directory)
    d = dict()
    for row in rows:
        name = str(row[0])
        values = list(map(float, row[1:]))
        d[name] = values
    return d

def load_lookerup_tables(filename="lookup_tables.csv", directory="data"):
    """Load lookup tables."""
    rows = load_file(filename, directory)
    d = dict()
    for row in rows:
        name, a, b, c, initial, pattern = row
        d[(name, int(a), int(b), int(c))] = (initial, pattern)
    return d

def load_pso_tables(filename="pso_gambler.csv", directory="data"):
    """Load lookup tables."""
    rows = load_file(filename, directory)
    d = dict()
    for row in rows:
        name, a, b, c, = str(row[0]), int(row[1]), int(row[2]), int(row[3])
        values = list(map(float, row[4:]))
        d[(name, int(a), int(b), int(c))] = values
    return d
