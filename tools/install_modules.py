#!/usr/bin/env python
import json
import os
import subprocess
import sys


PACKAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def install_modules(branch):
    # Try install modules
    for name in list_modules():
        try:
            code = install_module(name, branch)
        except Exception as ex:
            print 'Unable to install "%s" - %s' % (name, ex)
            continue

        # Process error returned
        if code != 0:
            print 'Unable to install "%s" - Process exited with return code: %s' % (name, code)
            continue

        # Module installed
        print 'Installed "NeApp/%s#%s"' % (name, branch)


def install_module(name, branch):
    return subprocess.call(
        ['npm', 'install', 'NeApp/%s#%s' % (name, branch)],
        shell=True
    )


def list_modules():
    with open(os.path.join(PACKAGE_DIR, 'package.json')) as fp:
        package = json.load(fp)

    for name in package.get('dependencies', {}):
        if not name.startswith('neon-extension-'):
            continue

        yield name


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'USAGE: install_modules.py BRANCH'
        sys.exit(1)

    install_modules(sys.argv[1])
