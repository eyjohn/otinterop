/* Generated by Cython 3.0a0 */

#ifndef __PYX_HAVE__simplehttp__ext
#define __PYX_HAVE__simplehttp__ext

#include "Python.h"

#ifndef __PYX_HAVE_API__simplehttp__ext

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C simplehttp::Response handle_request(PyObject *, simplehttp::Request const &);

#endif /* !__PYX_HAVE_API__simplehttp__ext */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initext(void);
#else
PyMODINIT_FUNC PyInit_ext(void);
#endif

#endif /* !__PYX_HAVE__simplehttp__ext */
