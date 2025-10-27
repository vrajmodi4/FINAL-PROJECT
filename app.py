# app.py
from flask import Flask, render_template, request
from crawler import get_links_and_forms
from sqli_test import test_url_for_sqli
from xss_test import test_url_for_xss

app = Flask(__name__)   # <- fixed here

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    target = ''
    if request.method == 'POST':
        target = request.form.get('url', '').strip()
        if target:
            # ensure scheme
            if not target.startswith('http'):
                target = 'http://' + target
            links, forms = get_links_and_forms(target)
            # include the base page too
            all_pages = set(links)
            all_pages.add(target)
            # Test each page for simple SQLi and XSS
            for page in list(all_pages):
                sqli = test_url_for_sqli(page)
                xss = test_url_for_xss(page)
                results.extend(sqli)
                results.extend(xss)
            # Also show detected forms (helpful to explain)
            for f in forms:
                results.append({
                    'vuln': 'Form Found (info)',
                    'url': f['page'],
                    'payload': None,
                    'evidence': f"form action={f['action']} method={f['method']} inputs={f['inputs']}"
                })
    return render_template('index.html', results=results, target=target)

if __name__ == '__main__':   # <- and fixed here
    app.run(debug=True)