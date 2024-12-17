from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="ciasAI",
    version="1.0.0",
    description="Pacote para análise de dados e sentimentos de companhias.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Emmanoel Cardoso",
    author_email="emmanoel@example.com",
    packages=find_packages(where=".", include=["ciasAI", "ciasAI.*"]),
    install_requires=requirements,
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)



