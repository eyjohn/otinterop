import signal
import threading
import time
import sys

import simplehttpserver
import simplehttpclient


from testtracer import Tracer
from opentracing import set_global_tracer, global_tracer
tracer = Tracer()
set_global_tracer(tracer)

if len(sys.argv) != 5:
    print("Usage: python server.py <address> <port> <ping_service_host> <ping_service_port>")
    sys.exit(1)

server = simplehttpserver.SimpleHttpServer(sys.argv[1], int(sys.argv[2]))
client = simplehttpclient.SimpleHttpClient(sys.argv[3], int(sys.argv[4]))


def cb(r):
    resp = client.make_request(
        simplehttpclient.Request(path='/ping', data=None))
    global_tracer().scope_manager.active.span.set_tag("app_tag", "value")
    return simplehttpserver.Response(200, ("Responding for: "+r.path+" ping service: "+repr(resp)).encode("ascii"))


def thread_func():
    server.run(cb)


x = threading.Thread(target=thread_func)
x.start()

sig = signal.sigwait([signal.SIGINT, signal.SIGTERM])

server.stop()
x.join()
