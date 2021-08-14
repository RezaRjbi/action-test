import pathlib
import os
import shutil
import nbformat
from nbconvert import HTMLExporter
PROJECTS_PATH = pathlib.Path('projects')
html_exporter = HTMLExporter()
html_exporter.template_name = 'classic'
ipynb_docs = list(PROJECTS_PATH.glob('**/*.ipynb'))

for ipynb in ipynb_docs:
    directory, file = os.path.split(ipynb)
    result_html = f'{os.path.splitext(file)[0]}.html'
    result_html_path = os.path.join(directory, result_html)
    nb = nbformat.reads(ipynb.read_text(), as_version=4)
    body, resources = html_exporter.from_notebook_node(nb)
    os.system(f'jupyter nbconvert --to html {ipynb.absolute()}')
    shutil.move(result_html_path, os.path.join('docs', result_html))

