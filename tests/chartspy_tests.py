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
    data = [{
                'value': x+1,
                'label': str('label {}').format(x),
                'fill_color': "#{}".format('ff0000' if x%2 == 0 else '0000ff')
            }
            for x in range(0, 10)
    ]
    bar_chart = create_bar_chart(svg, data, bar_spacing=10, margin=50)

    stringio = StringIO()
    bar_chart.to_png(stringio)
    hex = hashlib.md5(stringio.getvalue()).hexdigest()
    ref_hex = hashlib.md5(open(os.path.join(os.path.dirname(__file__), 'reference_bar_chart.png'), 'r').read()).hexdigest()
    eq_(ref_hex, hex)
