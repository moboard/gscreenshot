#!/usr/bin/env python

from setuptools import setup
import sys
import os

install_requires = [
    'pillow',
    # This currently throws an error. Install pygtk via your package manager.
    #'pygtk',
    'pygobject'
    ]

test_requires = [
    'nose',
    'mock'
    ]

data_files =[
        ('share/applications', ['dist/gscreenshot.desktop']),
        ('share/pixmaps', ['dist/gscreenshot.png'])
        ]


setup(name='gscreenshot',
    version='2.3.1',
    description='Lightweight GTK frontend to scrot',
    author='Nate Levesque',
    author_email='public@thenaterhood.com',
    url='https://github.com/thenaterhood/gscreenshot/archive/master.zip',
    install_requires=install_requires,
    tests_require=test_requires,
    entry_points={
        'gui_scripts': [
            'gscreenshot = gscreenshot:main'
        ]
    },
    test_suite='nose.collector',
    package_dir={'':'src'},
    packages=[
        'gscreenshot',
        'gscreenshot.resources',
        'gscreenshot.resources.gui',
        'gscreenshot.resources.gui.glade'
        ],
    data_files=data_files,
    package_data={
        '': ['*.glade', 'LICENSE']
        }
    )
