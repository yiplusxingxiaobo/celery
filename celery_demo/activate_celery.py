import os

if __name__ == "__main__":
    os.system('celery -A celery_app worker --loglevel=info')
