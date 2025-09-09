set -o errexit

# Install our dependencies
pip install -r requirements.txt

# Run our "shipping" command for static files
python manage.py collectstatic --no-input

# Run our database "construction" plan
python manage.py migrate

# for the creating superuser..
python manage.py shell -c "
from django.contrib.auth import get_user_model;
import os;
User = get_user_model();
username=os.environ.get('DJANGO_SUPERUSER_USERNAME','admin');
email=os.environ.get('DJANGO_SUPERUSER_EMAIL','admin@example.com');
password=os.environ.get('DJANGO_SUPERUSER_PASSWORD','admin123');
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password);
    print('Superuser created ✅');
else:
    print('Superuser already exists');
"