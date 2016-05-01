import hashlib
import os
import random
from StringIO import StringIO

from nose.tools import *

from chartspy.charts import create_bar_chart
from chartspy.svg import SVG


def test_basic_bar_chart():
    svg = SVG(800, 600)

    random.seed('8==D~')
    bar_chart = create_bar_chart(svg, [
        {
            'value': random.randint(5, 25),
            'label': '10-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '10-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '11-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '12-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '10-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '10-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '10-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '11-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
        {
            'value': random.randint(5, 25),
            'label': '12-10-2015',
            'fill_color': "#{}".format("".join(map(str, random.sample(range(1, 9), 6))))
        },
    ], bar_spacing=10, margin=50)

    stringio = StringIO()
    bar_chart.to_png(stringio)
    hex = hashlib.md5(stringio.getvalue()).hexdigest()
    ref_hex = hashlib.md5(open(os.path.join(os.path.dirname(__file__), 'reference_bar_chart.png'), 'r').read()).hexdigest()
    eq_(ref_hex, hex)
