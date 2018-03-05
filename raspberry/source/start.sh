#!/bin/bash
screen -dms test1 python MFRC522/Read.py
screen -dms test2 python inputHandler.py
