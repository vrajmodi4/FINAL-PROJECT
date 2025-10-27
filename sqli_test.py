# sqli_test.py
import requests

SQL_ERRORS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "mysql_fetch",
    "syntax error"
]

payloads = ["' OR '1'='1", "\" OR \"1\"=\"1", "'--", "' OR 1=1 --"]

def test_url_for_sqli(url):
    findings = []
    for p in payloads:
        try:
            test_url = f"{url}?id={requests.utils.requote_uri(p)}"
            resp = requests.get(test_url, timeout=5)
            text = resp.text.lower()
            for err in SQL_ERRORS:
                if err in text:
                    findings.append({
                        'vuln': 'SQL Injection',
                        'url': url,
                        'payload': p,
                        'evidence': err
                    })
        except Exception:
            continue
    return findings