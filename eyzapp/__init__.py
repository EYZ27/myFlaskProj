from flask import Flask


# 애플리케이션 팩토리 : create_app 함수가 app 객체를 생성해 반환
def create_app():
    app = Flask(__name__)

    from .views import main_views           # 상대참조: 같은 위치의 views 폴더에 main_views를 import
    app.register_blueprint(main_views.bp)

    return app