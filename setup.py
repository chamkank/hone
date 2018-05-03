import os
from setuptools import setup, find_packages

long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

setup(
    name='hone',
    version='0.1.3',
    author='Chamantha Kankanamge',
    author_email='chamkdev@gmail.com',
    license='MIT',
    description='Convert CSV to automatically nested JSON.',
    long_description=long_description,
    keywords="convert csv auto nested json",
    url='https://github.com/chamkank/hone',
    project_urls={
        "Source Code": 'https://github.com/chamkank/hone'
    },
    packages=find_packages(),
    install_requires=[],
    entry_points={'console_scripts': ['hone=hone.__main__:main']},
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ]
)

