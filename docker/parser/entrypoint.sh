#!/bin/bash
pip install -r requirements.txt
scrapyd
exec "$@"