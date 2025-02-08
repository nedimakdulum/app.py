from bs4 import BeautifulSoup
from serpapi import GoogleSearch

params = {
  "engine": "google",
  "q": "Google Scholar, Tuğçe Akdulum",
  "api_key": "11644446432bf95f012c85433e8b6730921d16f375573819788aadace840edb5"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]

html = "<html><body>"
for result in organic_results:
    title = result.get('title')
    link = result.get('link')
    snippet = result.get('snippet')
    result_html = f'<h3><a href="{link}">{title}</a></h3><p>{snippet}</p>'
    html += result_html
html += "</body></html>"

print(html)
