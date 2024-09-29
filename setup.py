from setuptools import setup, find_packages 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-16") as fh:
    requirements = fh.read()
    
setup(
    name = 'removecom',
    version = '0.0.1',
    author = 'Abraham T',
    author_email = 'abrahamg.tadesse@gmail.com',
    license = 'MIT LICENSE',
    description = 'This tool helps you delete all comments in a file',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/AbyTed/Comment-cleaner-CLI.git',
    py_modules = ['tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.12.6',
    classifiers=[
        "Programming Language :: Python :: 3.12.6",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
        'removecom = tool:cli',
        ]
    }
)