import transaction
from Queue import Queue
from threading import Thread
from skylines.lib import app_globals
from skylines.lib.xcsoar import analyse_flight
from skylines.model import DBSession


def start_analysis_worker(app):
    app_globals.config['analysis_queue'] = Queue()

    # start one worker thread
    t = Thread(target=worker)
    t.daemon = True
    t.start()

    return app


def worker():
    while True:
        flight = DBSession.merge(
            app_globals.config['analysis_queue'].get(),
            load=False
        )

        analyse_flight(flight, full=1024, triangle=4096)

        DBSession.flush()
        transaction.commit()

        app_globals.config['analysis_queue'].task_done()
