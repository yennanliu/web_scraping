import sys
sys.path.append(".")
from bs4 import BeautifulSoup
from celery_queue.IndeedScrapper.indeed_extract import (get_soup as get_soup_,
                                                        extract_company as extract_company_)

def test_get_soup():
    text = """<p>Here's a paragraph of text!</p>"""
    result = get_soup_(text)
    assert result.text.strip() == "Here's a paragraph of text!"


def test_extract_company():
    text = '<div class="row"><a class="result-link-source">google</a></div>'
    soup = BeautifulSoup(text)
    result = extract_company_(soup)
    # todo : add modified html to test extract company method
    assert result == 'NOT_FOUND'


if __name__ == '__main__':
    pytest.main([__file__])