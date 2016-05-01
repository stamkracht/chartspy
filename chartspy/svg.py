import xml.dom.minidom
from xml.etree.ElementTree import Element, tostring

import cairosvg
from six import iteritems


def create_element(tag_name, **kwargs):
    attributes = {
        key if key != 'klass' else 'class': str(value)
        for key, value in iteritems(kwargs)
        }
    return Element(tag_name, attributes)


class SVG(object):
    def __init__(self, width=600, height=400):
        self.width = width
        self.height = height
        self._root = Element(
            'svg',
            {
                'xmlns': "http://www.w3.org/2000/svg",
                'viewBox': "0 0 {} {}".format(width, height)

            }
        )

    def append(self, elm):
        self._root.append(elm)

    def extend(self, elms):
        self._root.extend(elms)

    def __str__(self):
        return tostring(self._root)

    def to_png(self, iowriter):
        cairosvg.svg2png(bytestring=str(self), write_to=iowriter)

    def toprettyxml(self):
        return xml.dom.minidom.parseString(str(self)).toprettyxml()
