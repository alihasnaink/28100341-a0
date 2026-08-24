import nbformat
import glob
import re

deps = set()
for f in glob.glob("notebooks/*.ipynb"):
    nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == 'code':
            lines = cell.source.split('\n')
            for line in lines:
                if '!pip install' in line or '%pip install' in line:
                    packages = re.findall(r'pip install.*? ([a-zA-Z0-9_-]+)', line)
                    if packages:
                        deps.update(packages)
                if line.startswith('import ') or line.startswith('from '):
                    match = re.match(r'^(?:import|from)\s+([a-zA-Z0-9_]+)', line)
                    if match:
                        deps.add(match.group(1))

print("Found dependencies:", sorted(deps))
