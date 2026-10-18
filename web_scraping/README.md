# Web Scraping Practice Pack

A beginner-to-intermediate practice folder using **requests** and **BeautifulSoup (bs4)**.

## Files

1. `01_requests_get.py` — make a GET request and inspect status, URL, and response.
2. `02_response_headers.py` — inspect response headers and content type.
3. `03_parse_page_title.py` — parse a page title with BeautifulSoup.
4. `04_select_links.py` — extract links from a page.
5. `05_quotes_life_tags.py` — collect quotes tagged `life` from all local HTML files in `scraped_data/`.
6. `06_extract_quotes_page.py` — scrape quote text, author, and tags from a public practice site.
7. `07_extract_table.py` — read an HTML table into records.
8. `08_find_by_class.py` — practice CSS selectors for classes and elements.
9. `09_pagination_quotes.py` — loop through paginated quote pages.
10. `10_download_image.py` — download an image from a URL you provide.
11. `11_save_to_csv.py` — save scraped quotes to CSV.
12. `12_user_agent_and_timeout.py` — use a User-Agent and request timeout.
13. `13_handle_errors.py` — handle HTTP and network errors.
14. `14_scrape_product_cards_demo.py` — practice extracting card-like elements from a sample page you own or are allowed to scrape.
15. `15_requests_json_api.py` — collect JSON from a public practice API.

## Notes

- Check a website's terms, robots.txt, and applicable laws before scraping.
- Prefer official APIs when available. Keep request rates low and do not bypass logins, paywalls, CAPTCHAs, or access controls.
- Public demo websites can change their HTML structure; selectors may need updating.
- The `scraped_data/` folder is for your own downloaded HTML files. Add your existing `quotes1.html`, `quotes2.html`, etc. there.
