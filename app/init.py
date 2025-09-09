from flask import Flask

def create_app():
    app = Flask(__name__)

    # 配置应用
    # app.config.from_object('config.Config')

    # 注册 Blueprint
    from app.views.remoteData import data_bp

    app.register_blueprint(data_bp, url_prefix='/data')  # 一级路由前缀

    return app