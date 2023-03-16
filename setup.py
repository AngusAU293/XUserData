from setuptools import setup, find_packages

setup(
    name='XUserData',
    version='1.0',
    description='A fake user data generator.',
    author='Angus Stuart',
    author_email='angus.stuart293@proton.me',
    url='https://github.com',
    packages=find_packages(),
    install_requires=[
        'random'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ]
)
