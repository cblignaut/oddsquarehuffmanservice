from setuptools import setup, find_packages

setup(
    name="oddsquarehuffmanservice",
    description="Odd square Huffman service",
    version="1.0.0",
    author="Cilliers Blignaut",
    author_email="",
    license="Proprietary",
    url="http://github.com/cblignaut/oddsquarehuffmanservice",
    packages=find_packages(),
    dependency_links=[],
    install_requires=[
        # Full requirements in requirements.txt. This is for reference.
    ],
    tests_require=["tox"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    zip_safe=False,
)
