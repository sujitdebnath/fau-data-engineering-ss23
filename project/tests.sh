#!/bin/bash

# Run component tests
echo "----------------------------------- Component Testing Started -----------------------------------"
python -m unittest tests/test_component.py
component_exit_code=$?
echo "----------------------------------- Component Testing Ended -----------------------------------"

echo ""

# Remove the generated SQLite file after component testing
echo "Remove the generated SQLite file after component testing (if exists)"
rm -f fau_data_engineering_ss23.sqlite

echo ""

# Run system tests
echo "----------------------------------- System Level Testing Started -----------------------------------"
python -m unittest tests/test_pipeline.py
system_exit_code=$?
echo "----------------------------------- System Level Testing Ended -----------------------------------"

echo ""

# Remove the generated SQLite file after system level testing
echo "Remove the generated SQLite file after system level testing (if exists)"
rm -f fau_data_engineering_ss23.sqlite

echo ""

# Check the exit code
if [ $component_exit_code -eq 0 ] && [ $system_exit_code -eq 0 ]; then
    echo "All tests passed!"
    exit_code=0
else
    echo "Some tests failed!"
    exit_code=1
fi

# Exit with the appropriate code
exit $exit_code