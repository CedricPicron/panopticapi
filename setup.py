# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

setup(
    name='panopticapi',
    packages=find_packages(),
    package_dir={'panopticapi': 'panopticapi'},
    install_requires=[
        'numpy',
        'Pillow',
    ],
    version='0.1',
)
