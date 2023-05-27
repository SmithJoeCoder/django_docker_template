import os
import sys

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "genesis.settings.base")

app = Celery("genesis")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

commands = " ".join(sys.argv)


if "--pool=gevent" in commands and "celery" in commands:
    import gevent
    import opencensus.common.runtime_context as runtime_context
    from psycogreen.gevent import patch_psycopg

    # Hardcode to set the threadlocal runtime context due to the issue
    # https://github.com/census-instrumentation/opencensus-python/issues/628

    if not gevent.monkey.is_module_patched("contextvars"):
        runtime_context.RuntimeContext = runtime_context._ThreadLocalRuntimeContext()

    patch_psycopg()

    import grpc.experimental.gevent as grpc_gevent

    grpc_gevent.init_gevent()
