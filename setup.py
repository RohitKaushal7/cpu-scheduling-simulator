from setuptools import setup, find_packages

setup(name='cpu-scheduling-simulator',
      version='1.0',
      packages=find_packages(),
      install_requires=['autopep8', 'cycler', 'kiwisolver', 'matplotlib',
                        'numpy', 'pycodestyle', 'pyparsing', 'python-dateutil', 'six', 'toml']
      )
