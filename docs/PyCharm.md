# PyCharm

## 設定手順

参考UR: https://pleiades.io/help/pycharm/using-docker-compose-as-a-remote-interpreter.html

#### Interpreter

1. 「⌘ + ,」を押下し、設定ファイルを開く
2. プロジェクト: <プロジェクト名> | Python インタープリターに移動する。
3. `Add Interpreter`をクリックし、`On Docker Compose`を選択
4. server: Docker, service: web(docker-composeのDjangoサービス名)を選択しNextをクリック
5. 推奨設定通りに進める

#### Run Configure

1. Django サーバーの実行 / デバッグ構成を作成(Run configure)
2. 下記の内容で設定する。DJANGO_SETTINGS_MODULE=djangoの設定ファイルを設定する(今回は、config.settings)
   ![run_configure.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fmf%2F48p1_fhn42sct8j4399wrmgr0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_Kj1SJN%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202023-05-06%203.59.48.png)
3. 設定したデバッグ構成が異常なく実行できることを確認
