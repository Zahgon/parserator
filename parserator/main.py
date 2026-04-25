import argparse
import glob
import os
import sys
import textwrap

import chardet
from lxml import etree

from . import data_prep_utils, manual_labeling, parser_template, training


def dispatch():

    pass


def label(args):
    pass


def train(args):
    pass


def init(args):
    pass


class XML(argparse.Action):
    def __call__(self, parser, namespace, string, option_string):
        try:
            with open(string) as f:
                tree = etree.parse(f)
                xml = tree.getroot()
        except OSError:
            xml = None
        except etree.XMLSyntaxError as e:
            if "Document is empty" not in str(e):
                raise argparse.ArgumentError(
                    self, "%s does not seem to be a valid xml file" % string
                )
            xml = None

        setattr(namespace, self.dest, string)
        setattr(namespace, "xml", xml)


def file_type(arg):
    pass


def training_data(arg):
    pass


class ModelFile(argparse.Action):
    def __call__(self, parser, namespace, model_file, option_string):
        module = namespace.module

        if hasattr(module, "MODEL_FILES"):
            try:
                model_path = module.__name__ + "/" + module.MODEL_FILES[model_file]
            except KeyError:
                msg = """
                      Invalid --modelfile argument
                      Models available: %s"""
                raise argparse.ArgumentTypeError(
                    textwrap.dedent(msg) % module.MODEL_FILES
                )
        else:
            raise argparse.ArgumentError(
                self, "This parser does not allow for multiple models"
            )

        setattr(namespace, self.dest, model_path)


def python_module(arg):
    pass
