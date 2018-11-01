from setuptools import setup
import glob
import os


# base package name
path_name = "opentargets_search_generator"

# load all version data hiden variables coming from version file to fill setup arguments
with open(path_name + os.path.sep + 'version.py') as fv:
      exec(fv.read())

# load requirements packages to be injected into setup function
required_pkgs = []
with open('requirements.txt') as f:
    required_pkgs.extend([x for x in f.read().splitlines() if not x.startswith("#")])

# full setup configuration
setup(name=__pkgname__,
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__author_email__,
      url=__homepage__,
      packages=[path_name],
      license=__license__,
      download_url=__homepage__ + '/archive/' + __version__ + '.tar.gz',
      keywords=['opentargets', 'bioinformatics', 'python3'],
      platforms=['any'],
      install_requires=required_pkgs,
      dependency_links=[],
      include_package_data=True,
      entry_points={
          'console_scripts': [__pkgname__ + '=' + path_name + '.cli:main'],
      },
      data_files=[],
      scripts=[],
      classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
      ],
      extras_require={
          'test': ['pytest', 'codecov']
      }
)