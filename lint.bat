@echo off
setlocal

echo ##########################" code pep8  ##########################"
pycodestyle --exclude=env --statistics .
echo ##########################" doc  pep8  ##########################"
pydocstyle --match='.*\\.py' --match-dir='^(?!env).*'

endlocal
