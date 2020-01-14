# OpenTracing C++/Python interoperability proof of concept

## Summary

This POC (proof of concept) describes how OpenTracing can be supported in an environment that mixes a Python with native extensions that utilise the native C++ implementation, which will be referred to as a **mixed platform** application environment. These ideas apply to other scenarios such as native Node.js modules or even across tightly coupled process barriers (e.g. fork/exec).

## Background Reading

This POC builds upon the concepts described in the [OpenTracing Specification](https://opentracing.io/specification/) and requires an understanding of Distributed Tracing. The book [Mastering Distributed Tracing](https://www.oreilly.com/library/view/mastering-distributed-tracing/9781788628464/) is a great resource for learning about Distributed Tracing fundamentals.

## Requirements

### Mixed platform applications produce similar-looking traces to single platform applications

An application written entirely in Python, or in C++, will often create only one `span` when handling a single request. In such a case both the libraries and application code may interact with this span. We will likewise expect that a span created in a mixed platform environment, e.g. in a C++ library, can be passed to Python and both platforms can interact with the span. In contrast, an implementation that creates two separate spans for each platform which reference each other would not be desired as this would change the behaviour of how an application is traced.

### Application and libraries rely only on standard tracing APIs

In the case of a native Python extension, we expect that a C++ library linked in by the extension will only use the standard C++ tracing APIs and will not be aware of any interoperability layer. The extension itself is expected to provide interoperability behaviour.

### Host platform owns the tracing implementation

Tracing interfaces such as OpenTracing enable the application to override the tracing implementation, such as loading a vendor-specific `Tracer` which handles tracing data. The host platform, in this example Python, will retain the ability to decide which implementation to use, and all extensions are expected to use this implementation.

### Performance impact of interoperability is understood and is not significant

Although difficult to quantify in absolute terms, it is expected that the tracing implementation avoids significant degradations in performance. In essence, implementations that for example synchronously cross-platform barriers for tracing API calls would be avoided. E.g. setting a tag in C++ would avoid invoking Python code synchronously.

### Multiple interoperable components can work simultaneously

In this example, multiple Python extensions can be loaded into the Python interpreter and are expected to continue to function. This would include extensions that may have been built with different but compatible tracing versions and may even share some runtime components, such as the same `.so`/`.DLL`.

## Design Considerations

### Tracing effects are deterministic or observable

### Tracing calls are write-only

### Tracing collection can be deferred

## Component Overview

## Test Scenario

## Outcome

## Unresolved issues
