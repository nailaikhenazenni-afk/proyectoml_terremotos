import json

# Let's inspect the contents of the notebook to understand the exact code, logic, results, and structure
with open('proyectoml_terremotos.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Summarize the cells to see what's in there
for i, cell in enumerate(notebook['cells']):
    cell_type = cell['cell_type']
    source = "".join(cell.get('source', []))
    print(f"--- Cell {i} ({cell_type}) ---")
    print(source[:200] + "..." if len(source) > 200 else source)