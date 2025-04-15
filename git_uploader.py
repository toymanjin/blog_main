import os
import subprocess
from datetime import datetime
import index_generator

today = datetime.now().strftime("%Y-%m-%d")
filename = f"{today}.html"
source_path = f"./generated/{filename}"

index_generator.generate_index()

repo_path = "."
os.chdir(repo_path)

subprocess.run(["git", "pull"])
subprocess.run(["cp", source_path, f"./{filename}"])
subprocess.run(["git", "add", filename])
subprocess.run(["git", "add", "index.html"])
subprocess.run(["git", "commit", "-m", f"자동 뉴스 업데이트: {filename} + 소개 포함 index"])
subprocess.run(["git", "push"])

print("🚀 GitHub Pages에 업로드 완료")
