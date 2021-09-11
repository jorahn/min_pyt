from setuptools import setup, find_packages

setup(
    name='minpt',
    version='0.1.0',
    url='https://github.com/jorahn/minpt.git',
    author='Jonathan Rahn',
    author_email='jonathan.rahn@42digital.de',
    description='Minimal Raw PyTorch Experiments',
    packages=find_packages(),
    install_requires=['torch == 1.9.0', 'torchvision == 0.10.0'],
)
