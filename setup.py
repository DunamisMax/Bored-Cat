from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bored-cat",
    version="1.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An interactive application with games to entertain cats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bored-cat",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyQt6>=6.5.0',
        'numpy>=1.21.0',  # If you used numpy for any calculations
    ],
    entry_points={
        'console_scripts': [
            'bored-cat=bored_cat.main:main',
        ],
    },
    package_data={
        'bored_cat': ['assets/images/*.png', 'assets/sounds/*.wav'],
    },
    include_package_data=True,
)