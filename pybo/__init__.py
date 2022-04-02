from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():  # 애플리케이션 팩토리 함수 => DB, url 호출, 필터 등 각종 확장기능 app에 부착하기
    app = Flask(__name__)
    app.config.from_object(config)  # config.py 파일에 작성한 항목을 app.config 환경 변수로 부르기 위해 해당 코드 추가.

    # ORM
    db.init_app(app)  # db 객체 초기화
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)  # migrate 객체 초기화
    from . import models

    # 블루 프린트
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime  # 'datetime' = 필터명

    # markdown
    Markdown(app, extentions=['nl2br', 'fenced_code'])
        # nl2br : 줄바꿈 문자를 <br>로 바꿔줌.
        # fenced_code :  코드 표시 기능

    return app
