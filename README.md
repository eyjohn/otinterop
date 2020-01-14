# otinterop

A prototype with several client/server applications that demonstrate interoperability of OpenTracing between C++ and Python.

## Dependencies

- [opentracing-cpp](https://github.com/eyjohn/opentracing-cpp/tree/thread_local_span_propagation) - OpenTracing C++ (with thread local scope manager)
- [w3copentracing-cpp](https://github.com/eyjohn/w3copentracing-cpp) - W3COpenTracing C++ (partial W3C compliant OpenTracing implementation)
- [w3copentracing-python](https://github.com/eyjohn/w3copentracing-python) - W3COpenTracing Python (partial W3C compliant OpenTracing implementation)
- [libsimplehttp](https://github.com/eyjohn/libsimplehttp) - A simple C++ library for HTTP Client/Servers wiht OpenTracing instrumentation
- [Cython](https://github.com/eyjohn/cython/tree/_std17_optional) - Cython with C++17 std::optional support
- [simplehttpclient-python](https://github.com/eyjohn/simplehttpclient-python) - Python wrapper around SimpleHttp Client with interop tracing support written in Cython
- [simplehttpserver-python](https://github.com/eyjohn/simplehttpserver-python) - Python wrapper around SimpleHttp Server with interop tracing support written in Cython
