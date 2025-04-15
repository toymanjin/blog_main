import os

def generate_index(directory="./generated"):
    files = sorted([f for f in os.listdir(directory) if f.endswith(".html")], reverse=True)

    content = """<!DOCTYPE html>
<html lang='ko'>
<head>
    <meta charset='UTF-8'>
    <title>ChatGPT 자동 뉴스 요약 블로그</title>
    <meta name='description' content='매일 아침 주식과 건강 뉴스 7개 요약 제공'>
</head>
<body>
    <h1>📰 ChatGPT 자동 뉴스 요약 블로그</h1>
    <p>이 페이지는 매일 아침 <strong>주식</strong>과 <strong>건강</strong> 뉴스를 자동 요약하여 발행하는 GitHub 기반 블로그입니다.</p>
    <p>광고가 노출되지 않더라도, 순수하게 정보를 제공하기 위한 실험적 프로젝트입니다.</p>
    <hr />
    <h2>📅 날짜별 뉴스 목록</h2>
    <ul>
"""

    for file in files:
        date = file.replace(".html", "")
        content += f"        <li><a href='{file}' target='_blank'>{date} 뉴스 보기</a></li>\n"

    content += """    </ul>
    <footer style='margin-top:30px;'>Powered by AI + GitHub</footer>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ 소개 포함 index.html 생성 완료")

if __name__ == "__main__":
    generate_index()
