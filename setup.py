from setuptools import setup, find_packages

setup(
    name='weather',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple weather checking application.',
    license='MIT',
    keywords='weather api',
)
