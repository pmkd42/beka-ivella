#!/bin/sh
python3 preprocessor.py
python3 recognize.py -video demo.mp4 
python3 trans.py
python3 app2.py
