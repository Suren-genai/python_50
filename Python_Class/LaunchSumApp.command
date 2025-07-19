#!/bin/zsh
cd "$(dirname "$0")"
source venv/bin/activate
/Library/Frameworks/Python.framework/Versions/3.11/bin/streamlit run Sum_Calculator.py
