from setuptools import setup, find_packages

setup(
    name='booklover',
    version='0.1',
    description='Booklover package',
    url='https://github.com/abhisingh5/hw09repo',
    author='Abhishek Singh',
    author_email='as4hfs@virginia.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
)