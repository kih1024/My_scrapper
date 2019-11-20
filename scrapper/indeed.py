import requests
from bs4 import BeautifulSoup
import time


LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    # print(indeed_result.text)
    soup = BeautifulSoup(result.text, "html.parser")
    # print(indeed_soup)
    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)
    links = pagination.find_all('a')
    # print(links)
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    # print(pages[:-1])
    # print(pages[0:5]) 인덱스 0부터 시작해서 5인덱스 전까지 가져온다.
    # span을 다 가져오되 마지막꺼는 제외한다.
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f"https://indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    # result = requests.get(f"{URL}&start={0*LIMIT}")
    # soup = BeautifulSoup(result.text, "html.parser")
    # results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for page in range(last_page):
        print(f"Scrapping Indeed Page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        # print(results)
        for result in results:
            # title=result.find("div",{"class": "title"})
            # anchor=title.find("a")["title"]
            # print(result)
            job = extract_job(result)
            jobs.append(job)
        # time.sleep(1)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(5)
    return jobs
