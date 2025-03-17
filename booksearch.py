import tkinter as tk
from tkinter import messagebox
import requests

def search_books():
    keyword1 = entry1.get().strip()
    keyword2 = entry2.get().strip()
    keyword3 = entry3.get().strip()

    keywords = [k for k in [keyword1, keyword2, keyword3] if k]  # 空のキーワードを除外
    if not keywords:
        messagebox.showinfo("エラー", "キーワードを入力してください")
        return

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    for search_word in keywords:
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_word}&maxResults=3"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            result_text.insert(tk.END, f"キーワード: {search_word}\n")
            display_results(data)
        except requests.exceptions.RequestException as e:
            result_text.insert(tk.END, f"エラー: {e}\n")

    result_text.config(state=tk.DISABLED)

def display_results(data):
    if "items" not in data:
        result_text.insert(tk.END, "書籍が見つかりませんでした\n")
        return
    else:
        for item in data["items"]:
            volume_info = item.get("volumeInfo", {})  # volumeInfoが存在しない場合の対策
            title = volume_info.get("title", "不明")
            authors = ",".join(volume_info.get("authors", ["不明"]))
            description = volume_info.get("description", "なし")
            result_text.insert(tk.END, f"タイトル: {title}\n")
            result_text.insert(tk.END, f"著者: {authors}\n")
            result_text.insert(tk.END, f"説明: {description}\n")
            result_text.insert(tk.END, "-" * 50 + "\n")

def clear_text():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

root = tk.Tk()
root.title("書籍検索")
root.geometry("600x400")

tk.Label(root, text="検索ワード1").pack(pady=2)
entry1 = tk.Entry(root, width=50)
entry1.pack(pady=2)

tk.Label(root, text="検索ワード2").pack(pady=2)
entry2 = tk.Entry(root, width=50)
entry2.pack(pady=2)

tk.Label(root, text="検索ワード3").pack(pady=2)
entry3 = tk.Entry(root, width=50)
entry3.pack(pady=2)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

search_button = tk.Button(button_frame, text="検索", command=search_books)
search_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="クリア", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

result_text = tk.Text(root, height=20, width=60, state=tk.DISABLED)
result_text.pack(pady=5)

root.mainloop()