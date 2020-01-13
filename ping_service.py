import signal
import threading
import time
import sys

from simplehttpserver import Request, Response, SimpleHttpServer

from testtracer import Tracer
from opentracing import set_global_tracer, global_tracer
tracer = Tracer()
set_global_tracer(tracer)

if len(sys.argv) != 3:
    print("Usage: python ping_server.py <address> <port>")
    sys.exit(1)

server = SimpleHttpServer(sys.argv[1], int(sys.argv[2]))


def cb(r):
    if r.path == "/ping":
        return Response(200, "pong".encode("ascii"))
    return Response(500, "The request wasn't a ping".encode("ascii"))


def thread_func():
    server.run(cb)


x = threading.Thread(target=thread_func)
x.start()

sig = signal.sigwait([signal.SIGINT, signal.SIGTERM])

server.stop()
x.join()
