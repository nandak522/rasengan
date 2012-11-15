import re
import get_latest_pkg_version
from distutils.version import LooseVersion

DEFAULT_INDEX_URL = 'http://pypi.python.org/simple/'

with open('source.txt') as f:
    for line in f.readlines():
        (name, version) = re.split(r'\W+[=]{1,2}\W+', line.strip())
        latest_version = get_latest_pkg_version.main(name, DEFAULT_INDEX_URL)
        if LooseVersion(latest_version) == LooseVersion(version):
            print name, 'is latest'
            continue
        elif LooseVersion(latest_version) > LooseVersion(version):
            print name, 'is old'
            continue
        elif LooseVersion(latest_version) < LooseVersion(version):
            print name, 'you have is latest, compared to the one in %s' % DEFAULT_INDEX_URL
