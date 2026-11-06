"""Build pma159/int_block.html (ISSB page) from final.json + issb_tpl.html.
usage: python3 build_int.py path/to/final.json"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'final.json'), encoding='utf8'))
tpl = open(os.path.join(here, 'issb_tpl.html'), encoding='utf8').read()
sys.path.insert(0, os.path.join(here, '..'))
from lz_build import lazy_block
out = lazy_block(tpl, 'issb', data, ['__issbRender'])
open(os.path.join(here, '..', 'issb_block.html'), 'w', encoding='utf8').write(out)
print(len(out))
