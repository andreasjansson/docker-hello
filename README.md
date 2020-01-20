hello
=====

Dummy HTTP service that responds with a message.

Environment variables
---------------------

* PORT
  - The port to listen on
  - Optional, defaults to 8080

* ENDPOINTS
  - Endpoint to message mapping
  - Format: "endpoint1:message1,endpoint2:message2,etc"
  - For example: "/:ok,/hello:world"
  - Optional, defaults to "/:hello"
