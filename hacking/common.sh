error_exit()
{
	echo "$1" 1>&2
	exit 1
}


find_python()
{
    PYTHON_BIN=$( which python3.8 2>/dev/null || which python3 2>/dev/null)

    if test $PYTHON_BIN; then
        echo "Found python at: $PYTHON_BIN"
        export PYTHON=$PYTHON_BIN
    else
        error_exit "No valid Python bin found"
    fi
}