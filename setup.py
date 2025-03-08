from setuptools import setup, find_packages

setup(
    name='lmstudio-client',
    version='0.1.0',
    author='Harshit',
    author_email='harshitkumar9030@gmail.com',
    description='A client library for interacting with the LM Studio API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/harshitkumar9030/lmstudio-client',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.25.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)