import os, fnmatch, yaml
from box import Box

PATTERN = "*.gitlab-ci.yml"

CURDIR = os.getcwd()


class Genepy(object):

    def __init__(self):
        # Do nothing
        pass

    def _scan_files(self):
        for root, dirs, files in os.walk(CURDIR):
            for filename in files:
                if fnmatch.fnmatch(filename, PATTERN):
                    print(os.path.join(root, filename))
                    # self._load_files(os.path.join(root, filename))
    
    def _load_files(self, filename):
        with open(filename) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            config = Box(config)
            print(config)


def scan():
    documentation = Genepy()
    print('Scanning Files....')
    documentation._scan_files()
    print('Scan Finished')
