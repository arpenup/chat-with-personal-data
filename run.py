from app import create_app, init_env

app = create_app()

with app.app_context():
    init_env()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], 
            host=app.config['HOST'], 
            port=app.config['PORT'],
            )