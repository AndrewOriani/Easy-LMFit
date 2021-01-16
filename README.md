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


If you don't want to use or setup Slab (non-Schusterlab people):
________________________________________________________________
Open a cmd window and run: python setup.py install

Then import easy_lmfit directly

~Andrew Oriani