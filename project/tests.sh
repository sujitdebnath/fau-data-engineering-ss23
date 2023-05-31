#!/bin/bash

# Run component tests
echo "----------------------------------- Component Testing Started -----------------------------------"
pdm run python -m unittest tests/test_component.py
echo "----------------------------------- Component Testing Ended -----------------------------------"

echo ""

# Run system tests
echo "----------------------------------- System Level Testing Started -----------------------------------"
pdm run python -m unittest tests/test_pipeline.py
echo "----------------------------------- System Level Testing Ended -----------------------------------"

echo ""

# Check the exit code
exit_code=$?
if [ $exit_code -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Some tests failed!"
fi

# Exit with the appropriate code
exit $exit_code
