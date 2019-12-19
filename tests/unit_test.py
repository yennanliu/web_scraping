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


html = """
    <table>
        <tr>
            <td class="image">
               <a href="/target/tt0111161/" title="Target Text 1">
                <img alt="target img" height="74" src="img src url" title="image title" width="54"/>
               </a>
              </td>
              <td class="title">
               <span class="company" data-caller-name="search" data-size="small" data-tconst="tt0111161">
               </span>
               <a href="/target/tt0111161/">
                Other Text
               </a>
               <span class="year_type">
                (2013)
               </span>
            </td>
        </tr>
    </table>
    """

def test_get_html():
    soup = BeautifulSoup(html)
    r = soup.find_all(name="span", attrs={"class":"company"})
    assert str(r) == '[<span class="company" data-caller-name="search" data-size="small" data-tconst="tt0111161">\n</span>]'

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


def test_extract_salary():
    text = '<div class="row"><a class="result-link-source">google</a></div>'
    soup = BeautifulSoup(text)
    result = extract_company_(soup)
    # todo : add modified html to test extract company method
    assert result == 'NOT_FOUND'


def test_extract_location():
    text = '<div class="row"><a class="result-link-source">google</a></div>'
    soup = BeautifulSoup(text)
    result = extract_company_(soup)
    # todo : add modified html to test extract company method
    assert result == 'NOT_FOUND'

if __name__ == '__main__':
    pytest.main([__file__])
