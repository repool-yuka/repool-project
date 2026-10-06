# Re Pool 採用LP

採用働き方BOOK（20ページ）の文章・条件・写真を元にした、PC・スマートフォン対応の静的Webページです。外部ライブラリや外部フォントへの接続は不要です。

## 表示

このディレクトリで `npm run dev` を実行し、ブラウザで `http://localhost:3000` を開きます。Python 3 と Node.js/npm を使用します。依存パッケージのインストールは不要です。`index.html` をブラウザで直接開くこともできます。

## ファイル

- `index.html`：日本語本文、ナビゲーション、資料閲覧・ダウンロード導線
- `styles.css`：PC・スマートフォン用のデザイン
- `script.js`：スマートフォンのメニュー操作
- `assets/`：PDFから抽出した元写真・カリキュラム・チェックシートと原本PDF

書体は端末の游明朝・ヒラギノ明朝、游ゴシック・メイリオ等を使用します。AI生成フォント・人物写真は使用していません。

## 掲載と連絡先

PDFの章順、給与・休日・資格・各種注記を保持しています。資料閲覧の案内や一部の導入文はWeb用に追加したものです。氏名等を非表示にした教材画像は添付PDFの素材をそのまま使用しています。

公式LINE・応募フォーム等のURLは資料にないため、架空の応募先は設定していません。現在のボタンは実際の働き方BOOKの閲覧・ダウンロードに接続しています。公開時に採用窓口を追加する場合は、確認済みのURLを使用してください。

静的ホスティングへ `index.html`、`styles.css`、`script.js`、`assets/` をまとめて配置できます。Web公開・外部サービス連携は未実施です。

## GitHub Pages公開

`.github/workflows/pages.yml` は手動実行の公開ワークフローです。コミットやpushだけでは公開されません。

1. GitHubリポジトリの Settings → Pages → Source を「GitHub Actions」に設定します。
2. Actions → Publish Re Pool recruitment page → Run workflow を実行します。
3. 成功した実行の `github-pages` に表示される公開URLを開きます。

公開対象は `index.html`・`styles.css`・`script.js`・`assets/` のみです。元PDFと写真も公開対象に含まれます。GitHub Pagesの利用可否はリポジトリの公開範囲と契約に依存します。リポジトリの公開範囲はこの作業では変更しません。

`python3 scripts/prepare-site.py /tmp/repool-site` で公開用ファイルを準備できます。出力先は空ディレクトリを指定してください。

## LINE案内（仮置き）

LINEのURLは未定です。画面下部のバーは「準備中」と表示し、ボタンは無効です。PDFのLINEバーにもリンクはありません。実URLが確定したら、Webでは `.line-button` を確認済みURLへのアンカーに置き換え、準備中表示を解除してください。PDFの各ページのバーにも同じ確認済みURLのリンク注釈を追加できます。

`assets/recruit-lp-soft-v3.pdf` は、全21ページの見出しに書体・サイズの強弱をつけ、写真の縁を柔らかくなじませ、LINEの仮バーを追加した版です。写真自体は変更せず、PDFの透明度処理で縁を背景になじませています。
