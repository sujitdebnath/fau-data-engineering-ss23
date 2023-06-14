#!/bin/bash

# Run component tests
echo "----------------------------------- Component Testing Started -----------------------------------"
pdm run python -m unittest tests/test_component.py
component_exit_code=$?
echo "----------------------------------- Component Testing Ended -----------------------------------"

echo ""

# Run system tests
echo "----------------------------------- System Level Testing Started -----------------------------------"
pdm run python -m unittest tests/test_pipeline.py
system_exit_code=$?
echo "----------------------------------- System Level Testing Ended -----------------------------------"

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