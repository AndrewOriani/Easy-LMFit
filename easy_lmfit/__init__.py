##############################################################################
# Python header

__author__ = "Andrew Oriani"
__copyright__ = "Copyright 2020"
__credits__ = ["Andrew E. Oriani"]
__license__ = "BSD-3-Clause"
__version__ = "1.0"
__maintainer__ = "Andrew Oriani Schusterlab"
__email__ = "oriani@uchicago.edu"
__url__ = r'schusterlab.uchicago.edu'
__status__ = "Dev-Production"

##############################################################################
#Checks module compatibility
try:
    import lmfit
    del lmfit
except (ImportError, ModuleNotFoundError):
    print('lmfit module not installed: $ conda  install -c conda-forge glob ')

import lmfit
from lmfit import *
from lmfit.models import (BreitWignerModel, ComplexConstantModel, ConstantModel, DampedHarmonicOscillatorModel, DampedOscillatorModel, DimensionalError,
DonaichModel, DoniachModel, ExponentialGaussianModel, ExponentialModel, ExpressionModel, GaussianModel, Interpreter, LinearModel, LognormalModel,
LorentzianModel, Model, MoffatModel, ParabolicModel, Pearson7Model, PolynomialModel, PowerLawModel, PseudoVoigtModel, QuadraticModel, RectangleModel,
SkewedGaussianModel, SkewedVoigtModel, SplitLorentzianModel, StepModel, StudentsTModel,ThermalDistributionModel, VoigtModel)
from . import  easy_lmfit
from .easy_lmfit import get_lm_models, get_model_params, lm_curve_fit

__all__=['easy_lmfit', 'get_lm_models', 'get_model_params', 'lm_curve_fit', 'BreitWignerModel',
'ComplexConstantModel',
'ConstantModel',
'DampedHarmonicOscillatorModel',
'DampedOscillatorModel',
'DimensionalError',
'DonaichModel',
'DoniachModel',
'ExponentialGaussianModel',
'ExponentialModel',
'ExpressionModel',
'GaussianModel',
'Interpreter',
'LinearModel',
'LognormalModel',
'LorentzianModel',
'Model',
'MoffatModel',
'ParabolicModel',
'Pearson7Model',
'PolynomialModel',
'PowerLawModel',
'PseudoVoigtModel',
'QuadraticModel',
'RectangleModel',
'SkewedGaussianModel',
'SkewedVoigtModel',
'SplitLorentzianModel',
'StepModel',
'StudentsTModel',
'ThermalDistributionModel',
'VoigtModel']
