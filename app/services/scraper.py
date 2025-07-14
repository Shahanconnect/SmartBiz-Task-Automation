from playwright.sync_api import sync_playwright
import re

def extract_price(text):
    match = re.search(r'[\d,.]+', text)
    if match:
        return match.group().replace(',', '')
    return None

def scrape_product_details(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 720})

        try:
            print(f"Navigating to {url}")
            page.goto(url, timeout=60000)
            page.wait_for_timeout(3000)

            def safe_text(selector):
                elem = page.query_selector(selector)
                return elem.inner_text().strip() if elem else None

            def safe_attr(selector, attr):
                elem = page.query_selector(selector)
                return elem.get_attribute(attr) if elem else None

            title = safe_text('#productTitle') or safe_text('h1')
            price = None
            for selector in [
                '#priceblock_dealprice',
                '#priceblock_ourprice',
                '#priceblock_saleprice',
                '.a-price .a-offscreen',
                '[data-testid="price"]',
                '.price', '.product-price'
            ]:
                raw = safe_text(selector)
                price = extract_price(raw) if raw else None
                if price:
                    break

            rating = safe_text('span.a-icon-alt') or safe_text('[data-testid="rating-stars"]')
            image_url = (
                safe_attr('#landingImage', 'src') or
                safe_attr('img[data-a-dynamic-image]', 'src') or
                safe_attr('img', 'src')
            )

            brand = (
                safe_text('#bylineInfo') or
                safe_text('.byline') or
                safe_text('[data-testid="brand"]')
            )

            availability = (
                safe_text('#availability span') or
                safe_text('.availability') or
                safe_text('.stock-status')
            )

            review_count = (
                safe_text('#acrCustomerReviewText') or
                safe_text('[data-testid="review-count"]') or
                safe_text('.review-count')
            )

            description = (
                safe_text('#productDescription') or
                safe_text('[data-testid="product-description"]') or
                safe_text('.product-description')
            )

            bullet_points = []
            for li in page.query_selector_all('#feature-bullets ul li span'):
                text = li.inner_text().strip()
                if text:
                    bullet_points.append(text)

            breadcrumbs = []
            for crumb in page.query_selector_all('#wayfinding-breadcrumbs_feature_div ul li span.a-list-item'):
                text = crumb.inner_text().strip()
                if text:
                    breadcrumbs.append(text)

            browser.close()

            if not title:
                return {'status': 'error', 'message': 'Failed to extract product title.'}

            return {
                'status': 'success',
                'title': title,
                'price': price,
                'rating': rating,
                'image_url': image_url,
                'brand': brand,
                'availability': availability,
                'review_count': review_count,
                'description': description,
                'bullet_points': bullet_points,
                'breadcrumbs': breadcrumbs
            }

        except Exception as e:
            browser.close()
            return {'status': 'error', 'message': f'Scraping failed: {str(e)}'}
