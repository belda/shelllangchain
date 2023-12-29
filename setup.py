import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Function to read the contents of requirements.txt
def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if not line.startswith('#') and line.strip()]

from version import __version__

setuptools.setup(
    name="shelllangchain",
    version=__version__,
    author="Belda",
    author_email="jakub.belescak@centrum.cz",
    description="Natural language to shell command converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/belda/shelllangchain",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "slc=shelllangchain.langchain_bash_helper:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires = load_requirements(),
)