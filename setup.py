import setuptools

setuptools.setup(
        name='tnpo',
        version='0.5.5',
        author='thisgary',
        author_email='gary.github@gmail.com',
        description='The cursed 3n+1 problem library.',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT Lisence',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.7',
        setup_requires=['pytest_runner'],
        tests_require=['pytest'],
        test_suite='tests',
)

