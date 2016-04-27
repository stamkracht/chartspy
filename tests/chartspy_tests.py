import hashlib
from StringIO import StringIO

from nose.tools import *

from chartspy.charts import create_bar_chart
from chartspy.svg import SVG


def test_basic_bar_chart():

    bar_chart = create_bar_chart(SVG(), [
        {
            'value': 10,
            'label': '10-10-2015'
        },
        {
            'value': 16,
            'label': '11-10-2015',
            'fill_color': '#ff0000'
        },
        {
            'value': 14,
            'label': '12-10-2015'
        },
    ])

    stringio = StringIO()
    bar_chart.to_png(stringio)
    hex = hashlib.md5(stringio.getvalue()).hexdigest()
    ref_hex = hashlib.md5(open('reference_bar_chart.png').read()).hexdigest()
    eq_(ref_hex, hex)
