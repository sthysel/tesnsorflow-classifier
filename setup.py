# -*- encoding: utf-8 -*-
import io
from glob import glob

from os.path import basename, dirname, join, splitext
from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='guido',
    version='0.0.1',
    description='Guidos peepers',
    long_description=read('README.md'),
    install_requires=[
        'click',
        'numpy',
        'scipy',
        'knobs',
    ],
    author='thys.meintjes',
    author_email='matthys.meintjes@bhp.com',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={
        'dedrowse': ['data/*.*'],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[],
    extras_require={},
    setup_requires=[],
    entry_points={
        'console_scripts': [
            'guido=guidos_eyes.:cli',
        ]
    },
)
