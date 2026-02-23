# 使用輕量級的 Python 映像檔
FROM python:3.10-slim

# 設定容器內的工作目錄
WORKDIR /app

# --- 新增：安裝 Git 以支援從 GitHub 下載的套件 ---
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
# --------------------------------------------

# 先複製依賴清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼
COPY . .

# 執行指令
CMD ["python", "main.py"]