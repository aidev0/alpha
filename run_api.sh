#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn api.main:app --reload 