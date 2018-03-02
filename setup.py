#!/usr/bin/env python

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def friendly(command_subclass):
	"""
	A decorator for classes subclassing one of the setuptools commands.

    It modifies the run() method so that it prints a friendly greeting.
	"""
	orig_run = command_subclass.run


	def midified_run(self):
		print "Hello, developer, how are you? :)"
		orig_run(self)

	command_subclass.run = modified_run
	return command_subclass


@friendly
class CustomDeveloperCommand(develop):
	print "Developer instalation"
	pass

@friendly
class CustomInstallCommand(install):
	print "User instalation"
	pass


setup(name='myPackage',
      version='0.1',
      description='My first python package',
      author='Marcelo Santos',
      author_email='email@domain.com',
      url='https://github.com/mefsantos/branch-testing',
      packages=['.', 'modules'],
      # Extension('foo', ['src/foo1.c', 'src/foo2.c']),
      install_requires=[
      "numpy",
      "pandas"
      ],
      cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDeveloperCommand,
      },
     )

