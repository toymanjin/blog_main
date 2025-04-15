import schedule
import time
import subprocess

def run_all():
    subprocess.run(["python3", "news_generator.py"])
    subprocess.run(["python3", "git_uploader.py"])

schedule.every().day.at("07:00").do(run_all)

print("⏰ 자동 뉴스 스케줄러 시작됨...")
while True:
    schedule.run_pending()
    time.sleep(60)
