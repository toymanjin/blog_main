import os
from datetime import datetime

# 오늘 날짜
today = datetime.now().strftime("%Y-%m-%d")

# 예시 뉴스 데이터 (요약 포함)
stock_news = [
    {
        "title": "삼성전자, AI 반도체 기대감에 강세",
        "summary": "AI 반도체 수요 증가에 대한 기대감이 삼성전자 주가를 끌어올렸습니다. 외국인 투자자들의 순매수도 긍정적인 영향을 주고 있습니다.",
        "url": "https://finance.naver.com/item/main.naver?code=005930"
    },
    {
        "title": "미국 CPI 발표 후 증시 상승세",
        "summary": "미국 소비자물가지수(CPI)가 예상보다 낮게 발표되며 금리 인상 우려가 완화되어 글로벌 증시가 반등세를 보이고 있습니다.",
        "url": "https://www.mk.co.kr/news/stock"
    }
]

health_news = [
    {
        "title": "비타민D, 면역력 강화 효과 입증",
        "summary": "최근 연구에 따르면 비타민D가 면역력 강화에 중요한 역할을 하며, 코로나19 예방 효과도 기대된다고 밝혔습니다.",
        "url": "https://health.chosun.com"
    },
    {
        "title": "스트레스 완화에 좋은 음식 5가지",
        "summary": "연어, 견과류, 다크초콜릿 등 스트레스를 완화시키는 데 도움을 주는 음식들이 소개되었습니다.",
        "url": "https://www.kormedi.com"
    }
]

# 광고 코드 (AdFit)
adfit_code = """
<div class="adfit-banner" style="text-align:center; margin: 20px 0;">
  <ins class="kakao_ad_area" style="display:none;"
    data-ad-unit = "DAN-HRoaYNJUpKQRTWQR"
    data-ad-width = "300"
    data-ad-height = "250"></ins>
  <script type="text/javascript" src="//t1.daumcdn.net/kas/static/ba.min.js" async></script>
</div>
"""

# HTML 본문 생성
def render_news_section(title, news_items):
    html = f"<h2>{title}</h2><div class='section'>\n"
    for item in news_items:
        html += f"""
        <div class='news-card'>
            <h3>{item['title']}</h3>
            <p>{item['summary']}</p>
            <a href="{item['url']}" target="_blank">📎 관련 기사 보기</a>
        </div>
        """
    html += "</div>\n"
    return html

# 전체 HTML 구성
html_content = f"""<!DOCTYPE html>
<html lang='ko'>
<head>
    <meta charset='UTF-8'>
    <meta name='description' content='ChatGPT 기반 매일 뉴스 요약 블로그 - 주식/건강 최신 소식 제공'>
    <title>{today} 오늘의 뉴스 요약</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; }}
        .news-card {{ border: 1px solid #ccc; padding: 15px; margin: 10px 0; border-radius: 8px; }}
        .news-card h3 {{ margin: 0; font-size: 18px; }}
        .news-card p {{ font-size: 15px; color: #333; }}
    </style>
</head>
<body>
    <h1>📰 {today} 오늘의 뉴스 요약</h1>
    {adfit_code}
    {render_news_section("📈 주식 뉴스", stock_news)}
    {render_news_section("💊 건강 뉴스", health_news)}
    <footer style="margin-top:40px;">Powered by 자동 뉴스봇</footer>
</body>
</html>
"""

# 저장 경로
output_dir = "./generated"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, f"{today}.html")

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ 요약 포함 카드형 HTML 저장 완료: {file_path}")
