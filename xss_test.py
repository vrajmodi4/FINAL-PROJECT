# xss_test.py
import requests

payloads = ["<script>alert('xss')</script>", "<img src=x onerror=alert(1)>"]

def test_url_for_xss(url):
    findings = []
    for p in payloads:
        try:
            test_url = f"{url}?q={requests.utils.requote_uri(p)}"
            resp = requests.get(test_url, timeout=5)
            if p in resp.text:
                findings.append({
                    'vuln': 'Reflected XSS',
                    'url': url,
                    'payload': p,
                    'evidence_snippet': resp.text[:300]
                })
        except Exception:
            continue
    return findings