"""Lazy-load helper: wraps a block's script so its big data is fetched from lz/<name>.json only when the page is first opened.
usage (from build scripts): lazy_block(tpl_html, name, data, render_fn) -> html"""
import json, hashlib, os
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, 'lz'), exist_ok=True)


def write_data(name, data):
    raw = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    v = hashlib.sha256(raw.encode()).hexdigest()[:12]
    for f in os.listdir(os.path.join(here, 'lz')):
        if f.startswith(name + '.'):
            os.remove(os.path.join(here, 'lz', f))
    open(os.path.join(here, 'lz', '%s.%s.json' % (name, v)), 'w', encoding='utf8').write(raw)
    return v


def lazy_block(tpl, name, data, fns):
    """tpl has '<script>\n(function(){\n  var D=@@DATA@@;' ... '})();\n</script>'. fns: global stubs to install, e.g. ['__intRender']"""
    v = write_data(name, data)
    head = '<script>\n(function(){\n  var D=@@DATA@@;'
    assert head in tpl, name
    a = tpl.index(head); b = tpl.rindex('})();\n</script>')
    body = tpl[a + len(head):b]
    stub = ''.join(
        "window.%s=function(el){if(el)el.innerHTML='<div style=\"padding:40px 16px;text-align:center;color:#64748b;font-weight:700\">Loading…</div>';"
        "window.__lzGet('%s','%s').then(function(D){if(!BOOTED){BOOTED=1;BOOT(D)}if(window.%s!==STUB_%s)return window.%s.apply(null,ARGS)}).catch(function(){if(el)el.innerHTML='<div style=\"padding:40px 16px;text-align:center;color:#b91c1c;font-weight:700\">Could not load. Check your internet and try again.</div>'});var ARGS=arguments};var STUB_%s=window.%s;"
        % (f, name, v, f, f, f, f, f) for f in fns)
    warm = ("setTimeout(function(){var n=0,t=setInterval(function(){n++;var ok=window.__acAdmin||(window.__acCats||[]).indexOf('%s')>-1;"
            "if(ok&&window.__lzGet){clearInterval(t);window.__lzGet('%s','%s').catch(function(){})}if(n>20)clearInterval(t)},1500)},3000);" % (name, name, v))
    js = ("<script>\n(function(){var BOOTED=0;\n" + stub + warm + "\nfunction BOOT(D){" + body + "}\n})();\n</script>")
    return tpl[:a] + js + tpl[b + len('})();\n</script>'):]
