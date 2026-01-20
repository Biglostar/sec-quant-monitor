import requests
from bs4 import BeautifulSoup
import time

url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&output=atom"
headers = {'User-Agent': 'Biglostar (darienk13@gmail.com)'}

print("SEC 실시간 공시 정밀 분석 중...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'xml')
    entries = soup.find_all('entry')
    
    found_count = 0
    for entry in entries:
        title = entry.title.text
        # f-string을 사용하여 링크 생성
        detail_link = f"https://www.sec.gov{entry.link['href']}"
        
        # 필터링 조건: RW(증자철회) 또는 4(내부자거래) 확인
        if 'RW' in title or '4 - ' in title:
            found_count += 1
            print(f"[{found_count}] 발견: {title}")
            print(f"🔗 링크: {detail_link}")
            
            # RW 공시인 경우에만 본문 정밀 분석 수행
            if 'RW' in title:
                print(f"   🔍 RW 본문 분석 시작...")
                time.sleep(0.1) # SEC 서버 예절 준수
                
                detail_res = requests.get(detail_link, headers=headers)
                if detail_res.status_code == 200:
                    detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
                    body_text = detail_soup.get_text().lower()
                    
                    if 's-1' in body_text:
                        print("   🚨 [High Impact] S-1 증자 철회 확인!")
                    elif 's-3' in body_text:
                        print("   ⚠️ [Medium Impact] S-3 증자 철회 확인!")
                    
                    if 'shares' in body_text:
                        print("   📈 발행 취소 주식수 데이터 존재 확인")
            
            print("-" * 60)
            
    if found_count == 0:
        print("현재 실시간 피드에 관심 공시가 없습니다.")
    else:
        print(f"분석 완료: 총 {found_count}개의 공시를 검토했습니다.")