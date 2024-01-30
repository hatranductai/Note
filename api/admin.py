from django.apps import apps
from django.contrib import admin

appList = ["api"]

for i in range(len(appList)):
    app = apps.get_app_config(appList[i])

    for model_name, model in app.models.items():
        admin.site.register(model)
