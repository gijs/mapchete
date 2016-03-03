#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='mapchete',
    version='0.0.1',
    description='tile-based geodata processing',
    author='Joachim Ungar',
    author_email='joachim.ungar@gmail.com',
    url='https://github.com/ungarj/mapchete',
    license='MIT',
    packages=[
        'mapchete',
        'static',
    ],
    scripts=[
        'cli/mapchete_execute.py',
        'cli/mapchete_serve.py'
    ],
    package_dir={'static': 'static'},
    package_data={'static':['index.html']},
    install_requires=[
        'tilematrix',
        'progressbar',
        'fiona',
        'pyyaml',
        'flask',
        'Pillow',
        'scipy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)
