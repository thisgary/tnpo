from setuptools import setup

setup(
        name='Collatz',
        packages=['collatz'],
        version='0.0-3-g5f5460a',
        description='The cursed Collatz conjecture library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

