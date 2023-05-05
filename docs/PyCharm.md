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
![run_configure.png](https://user-images.githubusercontent.com/79825084/236548269-ee9e5802-77d5-4030-8a63-f8ea980c539e.png)

3. 設定したデバッグ構成が異常なく実行できることを確認
