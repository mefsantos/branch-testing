#!/usr/bin/env python

from distutils.core import setup

setup(name='myPackage',
      version='0.1',
      description='My first python package',
      author='Marcelo Santos',
      author_email='email@domain.com',
      url='https://github.com/mefsantos/branch-testing',
      packages=['.', 'modules'],
      # Extension('foo', ['src/foo1.c', 'src/foo2.c']),
     )

