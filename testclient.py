import sys

from simplehttpclient import Request, Response, SimpleHttpClient

from testtracer import Tracer
from opentracing import set_global_tracer
tracer = Tracer()
set_global_tracer(tracer)

if len(sys.argv) != 4:
    print("Usage: python testclient.py <host> <port> <path>")
    sys.exit(1)

with tracer.start_active_span("testclient") as scope:
    scope.span.set_baggage_item("key", "val")
    client = SimpleHttpClient(sys.argv[1], int(sys.argv[2]))
    req = Request(sys.argv[3], None)
    resp = client.make_request(req)
    print("Received:", resp)
