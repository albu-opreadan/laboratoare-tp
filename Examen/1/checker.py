import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    if path.startswith('/'):
        return f'https://{host}{path}'
    else:
        return f'https://{host}/{path}'

    pass


def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    return url.startswith('https://')
    pass


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    response = requests.get(url, timeout=10)
    print("Status: ", response.status_code)
    print("Content-Type: ", response.headers["Content-Type"])
    pass


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try: 
        response = requests.get(url, timeout=5)
        return {"status": response.status_code, "content_type": response.headers["Content-Type"], "length": len(response.content), "server": response.headers["Server"]}
    except:
        return {"status": None, "error": "ceva nu a mers"}
    
    
    pass


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    lenSites = len(SITES)
    workingSitesNum = 0
    workingSites = []
    for site in SITES:
        if check_site(site)["status"] == 200:
            workingSitesNum = workingSitesNum + 1
            workingSites.append(site)
    workingSites.sort(key=lambda s: len(s))
    workingSites.reverse()
    print("Site-urile ce lucreaza sunt: ", workingSites)
    print("Number of working sites: ", workingSitesNum, "/", lenSites)

    pass


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    try:
        response = requests.get(url, timeout=5)
        present = [header for header in SECURITY_HEADERS if header in response.headers]
        missing = [header for header in SECURITY_HEADERS if header not in response.headers]
        score = int((len(present) / len(SECURITY_HEADERS)) * 100)
        return {
            "present": present,
            "missing": missing,
            "score": score
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": None,
            "error": str(e)
        }
    pass


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    for i in range(1, attempts + 1):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code < 500:
                return {"status": response.status_code, "attempts": i}
        except requests.RequestException:
            if i == attempts:
                return {"status": None, "error": "Connection error", "attempts": i}
    return {"status": 500, "attempts": attempts}
    pass
