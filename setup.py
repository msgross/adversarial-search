from setuptools import setup

setup(
    name='adversarial-search',
    url='https://github.com/msgross/adversarial-searching',
    author='Mark Gross',
    author_email='mark@grossremarks.com',
    packages=['algorithms'],
    install_requires=[],
    version='0.1',
    license='MIT',
    description='Implements a couple adversarial searches: random, minimax, alphabeta',
    long_description=open('README.md').read()
)
