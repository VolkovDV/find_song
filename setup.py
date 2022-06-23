from setuptools import find_packages, setup

from search_songs.main import version

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
      name='search-songs',
      version=version,
      description='Python Distribution Utilities',
      author='Dmitri Volkov',
      author_email='volkovdmvd@gmail.com',
      packages=find_packages(),
      install_requires=required,
      entry_points={
            'console_scripts': [
                  'search-songs=search_songs.main:main'
            ]
      },
      long_description=open('README.md').read(),
      )
