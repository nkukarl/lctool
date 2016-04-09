"""
leetcode commandline tool
"""
from setuptools import setup
import os

NAME = "lctool"
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

if not ISRELEASED:
    VERSION += '.dev'


def write_version_py(filename=NAME+'/version.py'):
    if os.path.exists(filename):
        os.remove(filename)
    cnt = """\
# THIS FILE IS AUTOMATICALLY GENERATED BY SETUP.PY
version = '%(version)s'
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()

write_version_py()

setup(
    name=NAME,
    version=VERSION,
    author="Hao Zhang",
    description=("commandline tool for leetcode"),
    packages=['lctool'],
    scripts=[],
    install_requires=[
        'BeautifulSoup',
    ],
    entry_points={
        'console_scripts': [
            'lc-get = lctool.run: lcget',
            'lc-submit = lctool.run: submit',
            ]
        },
    classifiers=[
        "Topic :: Utilities",
    ],
)
