from setuptools import setup

setup(
        name='Collatz',
        packages=['collatz'],
        version='0.0-6-g2762893',
        description='The cursed Collatz conjecture library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

