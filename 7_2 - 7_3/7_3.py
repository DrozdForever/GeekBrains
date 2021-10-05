from os import path, walk, listdir
from shutil import copytree

project_name = 'my_project'

try:
    for root, dirs, files in walk(project_name):
        if 'templates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                copytree(path.join(root, 'templates', entry),
                         path.join(project_name, 'templates', entry))
except FileExistsError:
    print('Работа с этими шаблонами уже проведена!')
