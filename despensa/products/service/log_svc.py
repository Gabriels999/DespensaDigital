import json

from ..models import ActivityLog


def log_login(user):
    logs = ActivityLog(
        type='login',
        logged_user=user,
    )
    logs.save()


def log_signup(user):
    logs = ActivityLog(
        type='signup',
        fromuser=user,
    )
    logs.save()


def log_logout(user):
    logs = ActivityLog(
        type='logout',
        logged_user=user,
    )
    logs.save()
