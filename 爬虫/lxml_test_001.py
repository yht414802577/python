# encoding: utf-8
"""
@version:??
@author:df
"""
from lxml import html
import cssselect

broken_html = '＜ul class =country>< li>Area< li>Population</ul＞'
tree = html.fromstring(broken_html)
fixed_html = html.tostring(tree, pretty_print=True)
print(fixed_html)

fixed_css = tree.cssselect('tr#places_area_row > td.w2p_fw')[0]
area = fixed_css.text_content()
print(area)