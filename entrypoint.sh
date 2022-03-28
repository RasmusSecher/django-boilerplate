#!/bin/bash
echo "--- Initiating entrypoint.sh ---"
echo ""
echo "Start makemigrations"
python src/manage.py makemigrations
echo "Makemigrations finished"
echo ""
echo "Start migrate"
python src/manage.py migrate --no-input
echo "Migrate finished"
echo ""
echo "--- Finished entrypoint.sh ---"

exec "$@"