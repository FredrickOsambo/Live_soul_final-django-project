"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()


#Ensuring User Authentication: Making sure signup, login, and logout are working perfectly.
#Article Management: Implementing the creation, viewing, and management of articles.
#User Profiles: Allowing users to view and edit their profiles.
#Doctor Profiles and Connections: Implementing doctor profiles and user-doctor connections.
#Styling and UI Enhancements: Ensuring the UI is responsive and looks good.
#Additional Features: Any additional features like nutrition and exercise suggestions.
