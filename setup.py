import setuptools
import os
import time

setuptools.setup(
    name='libertywrapper',
    version='1.0.1',
    author='Agape Ioan',
    author_email='contact@agapeioan.ro',
    description='Unofficial Python API Wrapper for Liberty.MP RageMP Server',
    keywords='libertymp, ragemp',
    long_description_content_type='text/markdown',
    url='https://github.com/AgapeIoan/LibertyWrapper',
    project_urls={
        'Source Code': 'https://github.com/AgapeIoan/LibertyWrapper',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT No Attribution License (MIT-0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)
