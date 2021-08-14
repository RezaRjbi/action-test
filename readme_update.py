import pathlib
import os
import shutil
import concurrent.futures

PROJECTS_PATH = pathlib.Path('projects')
ipynb_docs = list(PROJECTS_PATH.glob('**/*.ipynb'))


def main(ipynb):
    directory, file = os.path.split(ipynb)
    result_html = f'{os.path.splitext(file)[0]}.html'
    result_html_path = os.path.join(directory, result_html)
    os.system(f'jupyter nbconvert --to html {ipynb.absolute()}')
    shutil.move(result_html_path, os.path.join('docs', result_html))


with concurrent.futures.ThreadPoolExecutor() as executer:
    executer.map(main, ipynb_docs)
