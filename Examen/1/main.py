from checker import build_url, is_https, show_response, check_site, scan_sites, scan_sites, check_headers, retry_check

# Partea 1: apeluri pt build_url si is_https
print("   PARTEA 1")
print("* 1")
print(build_url("example.com", "login"))
print(build_url("example.com", "/login"))

print("* 2")
print("https://example.com is_https: ", is_https("https://example.com"))
print("example.com is_https: ", is_https("example.com"))

# Partea 2: apeluri pt show_response
print("   PARTEA 2")
show_response("https://example.com")

# Partea 3: apluri pt check_site
print("   PARTEA 3")
print("Outputul check_site: ", check_site("https://example.com"))
print("Outputul check_site: ", check_site("https://obviously-nu-exist.com"))

# Partea 4 apelul scan_sites
print("   PARTEA 4")
print("(asteptati un pic, poate sa dureze)")
scan_sites()

# Partea 5 apeluri prin check_headers

print("   PARTEA 5")
print(check_headers("https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff"))
print(check_headers("https://httpbin.org/response-headers?x-frame-options=DENY"))

# Partea 6 apeluri pentru retry_check
print("   PARTEA 6")

print(retry_check("https://httpbin.org/status/200"))
print(retry_check("https://httpbin.org/status/404"))
print(retry_check("https://httpbin.org/status/500"))
print(retry_check("https://httpbin.org/status/500", attempts=2))
print(retry_check("http://this-site-does-not-exist.invalid"))