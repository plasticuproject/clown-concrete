"""Setup file"""
from setuptools import setup  # type: ignore
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

VERSION = "1.9.9.9.9.9.9.9.9.9"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="concrete_calculator",
      packages=["concrete_calculator"],
      package_dir={"concrete_calculator": "concrete_calculator"},
      package_data={"concrete_calculator": ["py.typed", "__init__.pyi"]},
      version=VERSION,
      description="Concrete Volume Calculator",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="plasticuproject",
      author_email="plasticuproject@plasticuproject.com",
      keywords=["concrete", "calculator", "volume"],
      classifiers=[
          "Development Status :: 4 - Beta", "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3", "Topic :: Utilities"
      ],
      license="MIT",
      zip_safe=False,
      include_package_data=True)
