from random import choice
from os import listdir
from os.path import isfile, join

path = "../app/static/img/profile/default"

dirs = [f for f in listdir(path) if isfile(join(path, f))]
print(choice(dirs))