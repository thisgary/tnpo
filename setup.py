from setuptools import setup

setup(
        name='Collatz',
        packages=['collatz'],
        version='',
        description='The cursed Collatz conjecture library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

