#!/bin/bash

curl -XPOST http://askbob.test/api/from-user/ \
  -H "Content-type: application/json" \
  -d '{"sender": "test", "message": "hello"}'

