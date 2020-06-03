import os
from setuptools import setup, find_packages

setup(
    name='hone',
    version='0.1.9',
    author='Chamantha Kankanamge',
    author_email='chamkdev@gmail.com',
    license='MIT',
    description='Convert CSV to automatically nested JSON.',
    keywords="convert csv auto nested json",
    url='https://github.com/chamkank/hone',
    project_urls={
        "Source Code": 'https://github.com/chamkank/hone'
    },
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.0',
    entry_points={'console_scripts': ['hone=hone.__main__:main']},
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ]
)
