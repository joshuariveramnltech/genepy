# Copyright (C) 2020 Joshua Kim Rivera

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, fnmatch, yaml, argparse
from box import Box
from .htmlfactory import HtmlFactory
from .markdownfactory import MarkdownFactory


PATTERN = "*.gitlab-ci.yml"

CURDIR = os.getcwd()


class Genepy(object):

    def __init__(self):
        # Do nothing
        pass

    def _scan_files(self, target):
        for root, dirs, files in os.walk(target):
            for filename in files:
                if fnmatch.fnmatch(filename, PATTERN):
                    print(os.path.join(root, filename))
                    self._load_files(os.path.join(root, filename))
    
    def _load_files(self, filename):
        with open(filename) as f:
            jobs = yaml.load(f, Loader=yaml.FullLoader)
            # print(jobs)
            for job in jobs:
                for config in jobs[job]:
                    if config == 'only':
                        for variables in jobs[job][config]:
                            print(variables)
                            # for variable in jobs[job][config][variables]:
                            #     print(variable)
                        

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="sets the target directory", default=CURDIR)
    parser.add_argument("-s", "--scan_only", help="only perform scan for matching files on the target directory", default=False)

    args = parser.parse_args()
    print(args)

    documentation = Genepy()

    if args.scan_only.lower() == 'true':
        documentation._scan_files(args.directory)
