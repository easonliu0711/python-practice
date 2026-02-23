import os

folder_path = "/Users/liuyishen/Pictures/2602LiveLikeAYouth"

files_to_delete = []

# 掃描資料夾
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if "(1)" in file:
            full_path = os.path.join(root, file)
            files_to_delete.append(full_path)

# 顯示結果
print("以下檔案將被刪除：\n")
for f in files_to_delete:
    print(f)

print(f"\n共 {len(files_to_delete)} 個檔案")

# 確認刪除
confirm = input("\n確定刪除嗎？輸入 YES 繼續： ")

if confirm == "YES":
    for f in files_to_delete:
        os.remove(f)
    print("刪除完成")
else:
    print("已取消")
