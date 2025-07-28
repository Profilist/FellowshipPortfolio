#!/bin/bash

echo "Testing database..."

python -m unittest tests.test_db

if [ $? -eq 0 ]; then
    echo "Database tests passed"
else
    echo "Database tests failed"
    exit 1
fi

echo "Testing app..."

python -m unittest tests.test_app

if [ $? -eq 0 ]; then
    echo "App tests passed"
else
    echo "App tests failed"
    exit 1
fi

echo "All tests passed!"