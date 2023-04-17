from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
# 'main'은 별칭으로, 추후 'url_for' 함수에서 사용된다. __name__은 'main_views'가 인수로 전달된다.


@bp.route('/')          # app.route가 아닌, bp.route인 것에 주목
def hello_pybo():
    return 'Hello, Pybo!'