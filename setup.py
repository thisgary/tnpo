from setuptools import setup

setup(
        name='Collatz',
        packages=['collatz'],
        version='0.0-1-g621e8da',
        description='The cursed Collatz conjecture library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

