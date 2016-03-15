#! /bin/bash

python src/predict-one-one.py 1 >> Results/one-one.txt
python src/predict-one-one.py 2 >> Results/one-one.txt
python src/predict-one-one.py 3 >> Results/one-one.txt
python src/predict-one-one.py 4 >> Results/one-one.txt
python src/predict-one-one.py 5 >> Results/one-one.txt

python src/predict-one-all.py 1 >> Results/one-all.txt
python src/predict-one-all.py 2 >> Results/one-all.txt
python src/predict-one-all.py 3 >> Results/one-all.txt
python src/predict-one-all.py 4 >> Results/one-all.txt
python src/predict-one-all.py 5 >> Results/one-all.txt
