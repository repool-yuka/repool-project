#!/usr/bin/env python3
"""Copy only public website files into an isolated deployment directory."""
from pathlib import Path
import shutil
import sys

root = Path(__file__).resolve().parents[1]
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / 'dist'
if output == root or root.is_relative_to(output):
    raise SystemExit('Output must not contain the repository root')
output.mkdir(parents=True, exist_ok=True)
if any(output.iterdir()):
    raise SystemExit('Output directory must be empty; choose a new directory')
for name in ('index.html', 'styles.css', 'script.js'):
    shutil.copy2(root / name, output / name)
shutil.copytree(root / 'assets', output / 'assets')
(output / '.nojekyll').touch()
print(f'Prepared static website: {output}')
