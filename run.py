#!/usr/bin/env python

import os

from runners import sassc, node_sass

SPEC = 'repos/sass-spec-master/spec/basic/01_simple_css/input.scss'

sassc = sassc.Sassc()
node = node_sass.NodeSass()

specs = []

for root, _, files in os.walk('repos/sass-spec-master/spec'):
    if 'input.scss' in files:
        specs.append(root + '/input.scss')

map(sassc.run, specs)
map(node.run, specs)
