import sys
sys.path.append(".")
from celery_queue.IndeedScrapper.indeed_extract import get_soup as get_soup_


def test_get_soup():
    text = """<p>Here's a paragraph of text!</p>"""
    result = get_soup_(text)
    assert result.text.strip() == "Here's a paragraph of text!"



if __name__ == '__main__':
    pytest.main([__file__])