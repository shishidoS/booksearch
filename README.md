書籍検索アプリ

このアプリケーションは、Google Books API を使用して書籍を検索するGUIツールです。ユーザーは最大3つのキーワードを入力し、それに関連する書籍情報を取得できます。

機能

キーワードを最大3つまで入力し、関連する書籍情報を取得

書籍のタイトル、著者、説明を表示

書籍情報のクリア機能

エラーハンドリング対応

使用技術

Python

Tkinter（GUI構築）

Requests（APIリクエスト）

インストール方法

Python をインストール（バージョン 3.x 推奨）

必要なライブラリをインストール

pip install requests

app.py（スクリプトファイル）を実行

python app.py

使い方

アプリを起動する

「検索ワード1」「検索ワード2」「検索ワード3」にキーワードを入力（1つでも可）

「検索」ボタンを押すと、Google Books API を使用して書籍を検索

検索結果が画面に表示される

「クリア」ボタンで入力欄をリセット可能

注意事項

インターネット接続が必要です。

Google Books API の使用制限により、リクエスト回数が制限される場合があります。

ライセンス

このプロジェクトは MIT ライセンスのもとで提供されます。