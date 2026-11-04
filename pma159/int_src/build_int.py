"""Build pma159/int_block.html (Initial Interview page) from final.json + int_tpl.html.
usage: python3 build_int.py path/to/final.json"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'final.json'), encoding='utf8'))
tpl = open(os.path.join(here, 'int_tpl.html'), encoding='utf8').read()
out = tpl.replace('@@DATA@@', json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
open(os.path.join(here, '..', 'int_block.html'), 'w', encoding='utf8').write(out)
print(len(out))
