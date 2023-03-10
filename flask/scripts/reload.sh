#!/bin/sh

cd /home/app/calculator_wrapper/;
if [ -z $(/home/app/venv/bin/pip freeze | grep concrete-calculator==1.9) ]; then
        /home/app/venv/bin/poetry add --source fakepypi concrete_calculator;
fi;
/home/app/venv/bin/poetry update concrete_calculator;
/home/app/venv/bin/poetry install;
cd /home/app/;
supervisorctl restart flask
