from setuptools import setup, find_packages

setup(
    name='Hone',
    version='0.1',
    author='Chamantha Kankanamge',
    author_email='chamkdev@gmail.com',
    license='MIT',
    description='Convert CSV to automatically nested JSON.',
    keywords="convert csv to nested json",
    url='https://github.com/chamkank/hone',
    project_urls={
        "Source Code": 'https://github.com/chamkank/hone'
    },
    packages=find_packages(),
    package_data={'': ['*.csv', '*.json']}
)

