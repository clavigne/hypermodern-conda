import setuptools

setuptools.setup(
    name="hello_world",
    version="0.1.0",
    author="Cyrille Lavigne",
    author_email="",
    description="Hello, world!",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
)
