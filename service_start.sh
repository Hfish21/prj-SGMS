gunicorn --bind 0.0.0.0:8000 --timeout 120 --workers 3 DMK1_data_server:__hug_wsgi__ --daemon 
echo "<----- SERVER STARTING ----->"
