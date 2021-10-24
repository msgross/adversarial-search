"""
Setup adversarial search python package

This is fine
"""
from setuptools import setup


def get_description(filename):
    """ Method returns a long description from a given filename

    :param filename: The file to try to open for long description
    :return: string
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        return file.read()
    return ""

setup(
    name='adversarial-search',
    url='https://github.com/msgross/adversarial-searching',
    author='Mark Gross',
    author_email='mark@grossremarks.com',
    packages=['algorithms', 'utils'],
    install_requires=[],
    version='0.1',
    license='MIT',
    description='Implements a couple adversarial searches: random, minimax, alphabeta',
    long_description=get_description('README.md')
)
