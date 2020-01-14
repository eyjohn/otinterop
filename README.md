# otinterop

A prototype with several client/server applications that demonstrate interoperability of OpenTracing between C++ and Python.

For a summary of the purpose and discussion behind this proof-of-concept, please refer to [proof-of-concept](docs/poc.md) document. This README continues to describe how to build the dependencies and run the proof-of-concept.

## Installing Dependencies

### List of Dependencies

- [opentracing-cpp](https://github.com/eyjohn/opentracing-cpp/tree/thread_local_span_propagation) - OpenTracing C++ (with thread local scope manager)
- [w3copentracing-cpp](https://github.com/eyjohn/w3copentracing-cpp) - W3COpenTracing C++ (partial W3C compliant OpenTracing implementation)
- [w3copentracing-python](https://github.com/eyjohn/w3copentracing-python) - W3COpenTracing Python (partial W3C compliant OpenTracing implementation)
- [libsimplehttp](https://github.com/eyjohn/libsimplehttp) - A simple C++ library for HTTP Client/Servers wiht OpenTracing instrumentation
- [Cython](https://github.com/eyjohn/cython/tree/_std17_optional) - Cython with C++17 std::optional support
- [simplehttpclient-python](https://github.com/eyjohn/simplehttpclient-python) - Python wrapper around SimpleHttp Client with interop tracing support written in Cython
- [simplehttpserver-python](https://github.com/eyjohn/simplehttpserver-python) - Python wrapper around SimpleHttp Server with interop tracing support written in Cython

### Building and Installing dependencies

The following steps can be used to install all dependencies in order to run the test scenario.

#### 1. Build and Install C++ Dependencies

All dependencies can be built using the same process:

```sh
git clone $project
cd $project_dir
mkdir build
cd build
cmake ../
make
sudo make install
```

The packages should be installed in the following order:
- opentracing-cpp
- w3copentracing-cpp
- libsimplehttp


#### 2. Create virtual environment

All the modules can be built and installed into a Python virtual environment as follows:

```sh
git clone $otinterop_repo
cd $otinterop_dir
python3.8 -m venv venv
source venv/bin/activate
pip install wheel # required for some packages to be installed
```

Once activate each module can be installed locally by:
```sh
pip install /path/to/module/dir
```

The packages should be installed in the following order:
- Cython
- w3copentracing-python
- simplehttpclient-python
- simplehttpserver-python

## Running

### Test Applications

This repo contains:

- `testtracer` - package which provides a tracer implementation that prints captured traces to stderr
- `client.py` - Python application which uses the `simplehttpclient` to make a HTTP request within a span and collecting tracing data using a `testtracer`
- `ping_service.py` - Python application which uses `simplehttpserver` to provide a HTTP service which responds to the path `/ping` with a `pong` response, collecting tracing data using a `testtracer`
- `server.py` - Python application which uses `simplehttpserver` to provide a HTTP service which makes a HTTP request using a `simplehttpclient` to the ping service and then responds, collecting tracing data using a `testtracer`

### Test Scenario

These can be assembled to collect traces in the following scenario:

`client.py` (`simplehttpclient`) -> HTTP -> (`simplehttpserver`) `server.py` (`simplehttpclient`) -> HTTP -> (`simplehttpserver`) `ping_service.py`

#### Start service `ping_service.py`
```sh
python ping_server.py 0.0.0.0 8090 2> ping_server.traces
```
*NOTE: ctrl+c to collect tracing data*

#### Start service `server.py`
```sh
python server.py 0.0.0.0 8080 localhost 8090 2> server.traces
```
*NOTE: ctrl+c to collect tracing data*

#### Make HTTP request with `client.py`
```sh
python client.py localhost 8080 /hello 2> client.traces
```

After all these applications have been executed (and closed for the services), the tracing data can be reviewed.