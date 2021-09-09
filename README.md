# ポケモンデータベースbot「ともしびくん」

- ## はじめに
    「ともしびくん」はあなたのポケモンライフをより良いものにするポケモンデータベースDiscord botです

- ## 使い方
    - 導入方法
    1. このリポジトリをgit cloneする
       ```
       git clone https://github.com/ma2mo10/tmsb-kun/
       ```
    
    2. settingsの1行目のBot_tokenを[Discord Developer Portal](https://discord.com/developers/applications)で発行したBotトークンに置き換える

    3. 実行する
       ```
       python main.py
       ```

    - 機能
    1. ポケモン検索機能
       ともしびくんが導入されているDiscordサーバ上で次のコマンドを入力する
       ```
       /stats ポケモンの名前
       ```
       
       するとそのポケモンの種族値やタイプなどがBotから返ってくる

       使用例

       ![sample1](https://user-images.githubusercontent.com/32949045/132768008-afe4574e-2ad6-4c34-b942-194774960c00.png))
       
    2. 種族値からの逆引き

       種族値からポケモンを逆引きすることもできます
       ```
       /search 種族値の種類(hp, a, b, c, d , s) 種族値の値
       ```
       
       使用例

       ![tmsb-kun-sample2](https://user-images.githubusercontent.com/32949045/132768735-3c5bfe95-98bc-4114-b6c9-bdaff4295678.png)


- ## 使用ライブラリ
    [discord.py](https://github.com/Rapptz/discord.py)

- ## ポケモンデータ引用元
    使用したポケモンのデータはdayu282様が公開されている[poekmon-data.json](https://github.com/dayu282/pokemon-data.json)を使用させていただきました。
