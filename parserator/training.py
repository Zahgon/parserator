import os
import re
import textwrap
import time

import pycrfsuite
from lxml import etree

from . import data_prep_utils


def trainModel(
    training_data,
    module,
    model_path,
    params_to_set={"c1": 0.1, "c2": 0.01, "feature.minfreq": 0},
):

    pass


def renameModelFile(old_model):
    pass


def train(module, training_data, model_path):

    pass


def readTrainingData(file_locations, GROUP_LABEL):
    """
    Used in downstream tests
    """
    pass
