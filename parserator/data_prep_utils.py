import csv

from lxml import etree


class TrainingData:
    def __init__(self, xml=None, module=None):

        if xml is not None:
            self.xml = xml
            self._strip_formatting(self.xml)
        else:
            collection_tag = module.GROUP_LABEL
            self.xml = etree.Element(collection_tag)

        if module:
            self.parent_tag = module.PARENT_LABEL

    def append(self, labeled_sequence):
        pass

    def extend(self, labeled_sequences):
        pass

    def write(self, outfile):
        pass

    def _sequence_to_xml(self, labeled_sequence):
        pass

    def _xml_to_sequence(self, sequence_xml):
        pass

    # clears formatting for an xml collection
    def _strip_formatting(self, xml):
        pass

    def __iter__(self):
        for sequence_xml in self.xml:
            raw_text = etree.tostring(sequence_xml, method="text", encoding="unicode")
            yield raw_text, self._xml_to_sequence(sequence_xml)


# writes a list of strings to a file
def list2file(string_list, filepath):
    pass
