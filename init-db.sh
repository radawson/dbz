python -m flask db init
python -m flask db migrate -m "Initial migration."
python -m flask db upgrade