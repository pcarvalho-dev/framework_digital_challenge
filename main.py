import os

from application.app import create_app
from application.common.middlewares import LoggingMiddleware

app = create_app()
port = os.environ.get("API_PORT", "5000")

if __name__ == "__main__":
    app.logger.info("Application environment running at port %s", port)
    if os.environ.get("PRINT_REQUEST") == "True":
        app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(debug=True, host="0.0.0.0", port=port)
