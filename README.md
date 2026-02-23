# Python Practice & Homelab Automation

這是一個用於個人 Python 練習與 NAS 自動化腳本開發的集中式儲存庫。
開發環境架設於 Mac 本地，並直接將實體檔案映射至 Windows NAS (Dynabook) 進行 24/7 佈署與運行。

## 📁 Repository Structure (目錄結構)

* `wbc-ticket-scraper/`: WBC 2026 棒球賽事門票（日本 Tixplus）自動監控與 Telegram 警報系統。
* `clean_duplicates.py`: 系統檔案清理腳本。
* `hackerrank/`: HackerRank 演算法與資料結構練習題 (包含 NumPy)。
* `leetcode/`: LeetCode 刷題紀錄。

## 🛠️ Environment Setup (環境建置)

本專案使用 Python 虛擬環境隔離依賴套件。

1. 啟動虛擬環境 (Mac/Linux):
   ```bash
   source venv/bin/activate