from setuptools import setup

setup(
        name='3n+1',
        packages=['tnpo'],
        version='0.0-15-g88ec30d',
        description='The cursed 3n+1 problem library.',
        author='thisgary',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest_runner'],
        test_require=['pytest'],
        test_suite='tests',)

