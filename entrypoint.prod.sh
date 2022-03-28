#!/bin/bash
echo ""
echo "-------------------------------------"
echo "--- Initiating entrypoint.sh      ---"
echo ""
echo "--- Begin makemigrations          ---"
python src/manage.py makemigrations
echo "--- End makemigrations            ---"
echo ""
echo "--- Begin migrate                 ---"
python src/manage.py migrate --no-input
echo "--- End finished                  ---"
echo ""
echo "--- Begin static collection       ---"
python src/manage.py collectstatic --noinput
echo "--- End static collection         ---"
echo ""
echo "--- Finished entrypoint.sh        ---"
echo "-------------------------------------"
echo ""

exec "$@"