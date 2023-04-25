import setuptools
import os
import time

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

try:
    os.remove("C:\\Users\\John\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\libertywrapper.py-0.0.0-py3.9.egg")
except FileNotFoundError:
    pass

setuptools.setup(
    name='LibertyWrapper.py',
    author='Agape Ioan',
    author_email='contact@agapeioan.ro',
    description='Unofficial Python API Wrapper for Liberty.MP RageMP Server',
    keywords='libertymp, ragemp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AgapeIoan/LibertyWrapper.py',
    project_urls={
        'Source Code': 'https://github.com/AgapeIoan/LibertyWrapper.py',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
