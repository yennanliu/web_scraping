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

def test_get_soup():
    text = """<p>Here's a paragraph of text!</p>"""
    result = get_soup_(text)
    assert result.text.strip() == "Here's a paragraph of text!"

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

def test_extract_job_title():
    expected= 'NOT_FOUND'
    soup = BeautifulSoup(html)
    result = extract_job_title_(soup)
    assert result == expected

def test_extract_summary():
    expected= 'NOT_FOUND'
    soup = BeautifulSoup(html)
    result = extract_summary_(soup)
    assert result == expected

def test_extract_link():
    expected= 'NOT_FOUND'
    soup = BeautifulSoup(html)
    result = extract_link_(soup)
    assert result == expected

def test_extract_date():
    expected= '1 day ago'
    soup = BeautifulSoup(html)
    result = extract_date_(soup)
    assert result == expected

def test_extract_fulltext():
    expected= 'NOT_FOUND'
    soup = BeautifulSoup(html)
    result = extract_fulltext_(soup)
    assert result == expected

def test_get_full_job_link_():
    expected1 = 'https://www.indeed.com.sg/123'
    expected2 = 'https://jp.indeed.com/123'
    result1 = get_full_job_link_("123", city='Singapore')
    result2 = get_full_job_link_("123", city='Tokyo')
    assert result1 == expected1
    assert result2 == expected2


if __name__ == '__main__':
    pytest.main([__file__])
