from setuptools import setup

setup(
        name='Collatz',
        packages=['collatz'],
        version='0.0-4-g9f52c88',
        description='The cursed Collatz conjecture library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

