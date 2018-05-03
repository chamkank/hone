from setuptools import setup

setup(
    name='Hone',
    version='0.1.0',
    author='Chamantha Kankanamge',
    author_email='chamkdev@gmail.com',
    license='MIT',
    description='Convert CSV to automatically nested JSON.',
    keywords="convert csv auto nested json",
    url='https://github.com/chamkank/hone',
    project_urls={
        "Source Code": 'https://github.com/chamkank/hone'
    },
    packages=['hone'],
    install_requires=[],
    entry_points={'setuptools.installation': [
        'eggsecutable = hone:__main__'
    ]},
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ]
)

