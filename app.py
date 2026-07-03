from flask import Flask, Response, render_template, request, flash
from urllib.parse import urlparse
import pyshorteners
import re

app = Flask(__name__)
app.secret_key = "secret_key"
SITE_URL = "https://urlmasking.vercel.app"

# Initialize the URL shorteners
s = pyshorteners.Shortener()
shorteners = [s.tinyurl, s.dagd, s.clckru, s.osdb]

# Validation functions
def validate_web_url(url):
    url_pattern = re.compile(
        r'^(https?://)'  # starts with 'https://'
        r'([a-zA-Z0-9-]+\.)*'  # optional subdomains
        r'([a-zA-Z]{2,})'  # domain
        r'(:\d{1,5})?'  # optional port
        r'(/.*)?$'
    )
    if not url_pattern.match(url):
        raise ValueError("Invalid URL format. Please provide a valid web URL.")

def validate_custom_domain(domain):
    domain_pattern = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not domain_pattern.match(domain):
        raise ValueError("Invalid custom domain. Please provide a valid domain name.")

def format_phish_keywords(keywords):
    max_length = 15
    if not isinstance(keywords, str):
        raise TypeError("Keywords must be a string.")
    if " " in keywords:
        raise TypeError("Phishing keywords should not contain spaces. Use '-' to separate them.")
    if len(keywords) > max_length:
        raise ValueError("Keywords exceed the maximum allowed length.")
    return "-".join(keywords.split())

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get inputs from form
            web_url = request.form.get("web_url")
            custom_domain = request.form.get("custom_domain")
            phish_keywords = request.form.get("phish_keywords")

            # Validate inputs
            validate_web_url(web_url)
            validate_custom_domain(custom_domain)
            phish_keywords = format_phish_keywords(phish_keywords)

            # Generate short URLs and mask them
            short_urls = []
            for shortener in shorteners:
                try:
                    short_url = shortener.short(web_url)
                    short_urls.append(mask_url(custom_domain, phish_keywords, short_url))
                except:
                    continue

            if not short_urls:
                flash("Unable to shorten the URL with the available services.", "error")
            return render_template("index.html", original_url=web_url, masked_urls=short_urls)

        except Exception as e:
            flash(str(e), "error")
    
    return render_template("index.html")

@app.route("/robots.txt")
def robots_txt():
    return Response(
        "User-agent: *\nAllow: /\n\nSitemap: https://urlmasking.vercel.app/sitemap.xml\n",
        mimetype="text/plain",
    )

@app.route("/sitemap.xml")
def sitemap_xml():
    return Response(
        """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://urlmasking.vercel.app/</loc>
  </url>
</urlset>
""",
        mimetype="application/xml",
    )

@app.route("/googlef62cf14d0321ed1e.html")
def google_site_verification():
    return Response(
        "google-site-verification: googlef62cf14d0321ed1e.html",
        mimetype="text/html",
    )

if __name__ == "__main__":
    app.run(debug=True)
