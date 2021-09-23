

method1(){
    # Build, view, install, and test the wheel
    python setup.py bdist_wheel
    unzip -l dist/my_python_package-1.0.0-*.whl

    pip install dist/my_python_package-1.0.0-*.whl

    pip uninstall my_python_package

    python -c "import my_python_package"

}
