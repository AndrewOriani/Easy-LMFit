'''
Welcome to LMFit! The LMFit module is a warpper of the LM fitting library. 
The main purpose of this module is to create an easy to use interface for 
the LM library that allowed for easy access to it's abundant feature set. This 
functionality is backwards compatible with the scipy curve_fit syntax and uses the
same minimization engine, meaning that it is both a drop in replacement for and 
will give the same results as curve_fit. The module however provides a the abilty
to tak eadvantage of the more advanced features of the LM library in an a-la carte
fashion. These include advanced statistical analysis, constraints and the ability
to easily override fit parameters ad-hoc. To learn more about these features and
other advantages of the LM library check out the LMFit demos in the tutorial notebook
folder. For more questions please email me! 

~Andrew Oriani

'''

from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.absolute()

# Get the long description from the README file
with open(here / "README.md", encoding="utf-8") as f:
    long_description = f.read()

with open(here / "requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

doclines = __doc__.split('\n')

setup(name='easy_lmfit',
      version='1.0',
      description = doclines[0],
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Andrew E. Oriani',
      packages=find_packages(),
      author_email='oriani@uchicago.edu',
      maintainer='Andrew Oriani SchusterLab',
      license='BSD-3-Clause',
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows::Only",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Environment :: Console"],
      python_requires=">=3.5, <4",
      # install_requires=['numpy', 'IPython'],
      install_requires=requirements
      )
