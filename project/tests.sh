#!/bin/bash

# Run component tests
pdm run python -m unittest tests/test_component.py

# Run system tests
pdm run python -m unittest tests/test_pipeline.py

# Check the exit code
exit_code=$?
if [ $exit_code -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Some tests failed!"
fi

# Exit with the appropriate code
exit $exit_code
