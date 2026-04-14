# lms_project package

# Import Celery app only if celery is installed (for CI/CD and production without forcing celery)
try:
    from .celery import app as celery_app
    __all__ = ('celery_app',)
except ImportError:
    # Celery not installed (e.g. in minimal CI environment)
    celery_app = None
    __all__ = ()