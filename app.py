import settings
from web_report.app import app

if __name__ == '__main__':
    app.config.from_object(settings.Config)
    app.run()
