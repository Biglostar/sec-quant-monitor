import requests
from bs4 import BeautifulSoup

url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&output=atom"
headers = {'User-Agent': 'Biglostar (darienk13@gmail.com)'}

print("SEC 실시간 공시 분석 중...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # XML 데이터를 파이썬이 이해하기 쉽게 요리하기
    soup = BeautifulSoup(response.text, 'xml')
    entries = soup.find_all('entry')
    
    found_count = 0
    for entry in entries:
        title = entry.title.text
        link = entry.link['href']
        
        # 필터링 조건: RW(증자철회) 또는 4(내부자거래)가 제목에 포함되어 있는지 확인
        if 'RW' in title or '4 - ' in title:
            print(f"[{found_count + 1}] 발견: {title}")
            print(f"🔗 링크: https://www.sec.gov{link}")
            print("-" * 50)
            found_count += 1
            
    if found_count == 0:
        print("현재 실시간 피드에 RW 또는 Form 4 공시가 없습니다.")
    else:
        print(f"총 {found_count}개의 관심 공시를 발견했습니다.")