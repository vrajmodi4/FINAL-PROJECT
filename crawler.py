# crawler.py
import requests
from bs4 import BeautifulSoup
import urllib.parse

def normalize(url):
    return url.rstrip('/')

def get_links_and_forms(base_url, max_pages=30):
    base_url = normalize(base_url)
    to_visit = [base_url]
    visited = set()
    links = set()
    forms = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)
        try:
            resp = requests.get(url, timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
        except Exception:
            continue

        # collect links
        for a in soup.find_all('a', href=True):
            link = urllib.parse.urljoin(url, a['href'])
            if link.startswith(base_url):
                link = normalize(link)
                if link not in visited:
                    to_visit.append(link)
                links.add(link)

        # collect forms
        for form in soup.find_all('form'):
            action = form.get('action')
            method = form.get('method', 'get').lower()
            inputs = []
            for inp in form.find_all('input'):
                name = inp.get('name')
                if name:
                    inputs.append(name)
            forms.append({
                'page': url,
                'action': urllib.parse.urljoin(url, action) if action else url,
                'method': method,
                'inputs': inputs
            })

    return list(links), forms