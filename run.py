from app import create_app, init_env
from app.utils.common import open_browser

app = create_app()

with app.app_context():
    init_env()

if __name__ == "__main__":
    open_browser(app) #

    app.run(debug=app.config['DEBUG'], 
            host=app.config['HOST'], 
            port=app.config['PORT'],
            use_reloader=True) # 显式启用 reloader