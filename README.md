# FINAL-PROJECT
 Automated Web Vulnerability Scanner

 Abstract:
This report details the design, implementation, and conclusion of an automated web vulnerability
scanner and crawler project. The primary objective was to create a Python-based application capable
of discovering and mapping a target website’s structure, identifying key elements like links and
forms, and performing baseline security testing for common flaws, specifically simple SQL Injection
(SQLi) and Reflected Cross-Site Scripting (XSS). The project is structured into modular components: a
Flask web interface for user interaction, a dedicated crawler for site mapping, and separate testing
modules for each vulnerability type. The resulting tool provides a foundational, extensible framework
for preliminary security assessments of web applications.

1 Introduction:
In the modern digital landscape, web applications are primary targets for malicious actors.
Automated security testing is a critical practice for early vulnerability detection and mitigation. This
project was initiated to develop a lightweight, functional tool that automates the initial phase of a
security audit. The resulting application, built primarily in Python, integrates web crawling capabilities
with basic vulnerability analysis. By automatically navigating a target site and injecting known
malicious payloads into URL parameters, the scanner aims to quickly identify potential weak points,
providing developers and security analysts with immediate, actionable feedback on a site’s security
posture.

2 Tools Used:
The project was built using the following core technologies and libraries, each serving a specific
function:
• Python 3: The foundational programming language used for the entire application logic.
• Flask: A micro web framework used to create the server-side application (app.py), providing a
simple web interface for accepting target URLs and displaying scan results.
• Requests: A robust HTTP library essential for making GET and POST requests. It was utilized in
both the crawler.py module for fetching pages and in the testing modules (sqli_test.py and
xss_test.py) for injecting payloads and analyzing responses.
BeautifulSoup4 (BS4): A Python library for pulling data out of HTML and XML files. It was critical in
crawler.py for parsing HTML content, identifying all internal links, and extracting attributes (like
action, method, and input names) from HTML forms.


3 Steps Involved in Building the Project:
The project followed a modular development approach, ensuring separation of concerns and ease of
maintenance:
1. Core Application Framework (app.py):
The development began by setting up a basic Flask application to serve as the user interface. It
handles a simple form to accept the target URL, validates the input, and acts as the orchestrator by
calling the crawler and testing functions. It collects and structures all findings before rendering them
to the user.
2. Web Crawler Module (crawler.py):
This module was implemented to map the site structure. It uses the requests library to fetch the initial page and
BeautifulSoup4 to parse the HTML. The core function, get_links_and_forms, recursively discovers internal links
(up to a set limit) and identifies all HTML forms on visited pages. It normalizes URLs to ensure consistency in
scanning.
3. SQL Injection Test Module (sqli_test.py):
The SQLi module implements a basic error-based detection technique. It defines a list of common
SQL error strings (e.g., “syntax error,” “mysql_fetch”) and pre-defined injection payloads (e.g., &#39; OR
&#39;1&#39;=&#39;1). It iterates over the target URLs, appending a URL parameter with the payload, and checks the
response text for any of the defined error strings. A match indicates a high probability of a SQLi
vulnerability.
4. XSS Test Module (xss_test.py):
The XSS module focuses on detecting Reflected XSS. It uses non-intrusive test payloads (e.g., &lt;script&gt;
alert(&#39;xss&#39;) &lt;/script&gt;) and injects them into URL parameters. If the raw payload string is found
unescaped in the resulting page’s HTML body, the module flags it as a potential Reflected XSS
vulnerability.
5. Integration and Refinement:
The final phase involved integrating the modules in app.py. The core logic ensures that every
discovered page, including the entry page, is subjected to both SQLi and XSS tests. Error handling was
implemented (using try-except blocks in the testing modules) to gracefully manage network failures
or application timeouts during the scanning process.

Conclusion:
The Automated Web Vulnerability Scanner project successfully delivered a working prototype capable of performing foundational security assessments. By combining robust web crawling with specific vulnerability testing for SQLi and XSS, the application efficiently provides a first-line defense tool. While the current implementation is limited to simple parameter-based attacks and error-based detection, it provides a solid and extensible architecture. Future work could involve expanding the scope to include testing of HTML forms, incorporating more sophisticated attack vectors (e.g., Blind SQLi, Stored XSS), and enhancing the reporting interface for clearer visualization of the risk and findings.
