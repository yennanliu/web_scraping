import unittest
import sys
sys.path.append(".")
from bs4 import BeautifulSoup
from celery_queue.IndeedScrapper.indeed_extract import (get_soup as get_soup_,
                                                        extract_company as extract_company_,
                                                        extract_salary as extract_salary_,
                                                        extract_location as extract_location_,
                                                        extract_job_title as extract_job_title_,
                                                        extract_summary as extract_summary_,
                                                        extract_link as extract_link_,
                                                        extract_date as extract_date_,
                                                        extract_fulltext as extract_fulltext_,
                                                        write_logs as write_logs_,
                                                        get_full_job_link as get_full_job_link_)


with open('tests/unittest_data.txt', 'r') as file:
  html = file.read()

# def test_get_html():
#     soup = BeautifulSoup(html)
#     r = soup.find_all(name="span", attrs={"class":"company"})
#     assert str(r) == '[<span class="company" data-caller-name="search" data-size="small" data-tconst="tt0111161">\n</span>]'

# def test_get_soup():
#     text = """<p>Here's a paragraph of text!</p>"""
#     result = get_soup_(text)
#     assert result.text.strip() == "Here's a paragraph of text!"

def test_extract_company():
    expected = '\\n\\nU3 INFOTECH PTE. LTD.'
    soup = BeautifulSoup(html)
    result = extract_company_(soup)
    assert result == expected

def test_extract_salary():
    expected = 'NOT_FOUND'
    soup = BeautifulSoup(html)
    result = extract_salary_(soup)
    assert result == expected

def test_extract_location():
    expected= 'Shenton Way'
    soup = BeautifulSoup(html)
    result = extract_location_(soup)
    assert result == expected

if __name__ == '__main__':
    pytest.main([__file__])
