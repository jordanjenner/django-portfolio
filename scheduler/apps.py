from django.apps import AppConfig
from projects.models import Project
from datetime import datetime
import pytz
from django.conf import settings
import json
from urllib.request import urlopen


class SchedulerConfig(AppConfig):
    name = 'scheduler'


class RepoPuller():
    def __init__(self):
        self.repos = self.get_json()
        self.import_data()

    def import_data(self):
        for repo in self.repos:
            if repo["owner"]["login"] == "jordanjenner":
                repo_id = repo["id"]
                name = repo["name"]
                url = repo["svn_url"]
                creation_date = repo["created_at"]
                creation_date = self.date_convert(creation_date)
                last_updated = repo["updated_at"]
                last_updated = self.date_convert(last_updated)
                description = repo["description"]
                language = repo["language"]
                is_private = repo["private"]

                try:
                    project = Project.objects.get(repo_id=repo_id)

                    project.repo_id = repo_id
                    project.repo_url = url
                    project.name = name
                    project.creation_date = creation_date
                    project.last_updated = last_updated
                    project.description = description
                    project.language = language
                    project.is_private = is_private

                    project.save()

                except Project.DoesNotExist:
                    Project.objects.create(
                        repo_id=repo_id,
                        repo_url=url,
                        name=name,
                        creation_date=creation_date,
                        last_updated=last_updated,
                        description=description,
                        language=language,
                        is_private=is_private
                        )

    def date_convert(self, strdate):
        dformat = "%Y-%m-%dT%H:%M:%SZ"
        unaware_date_object = datetime.strptime(strdate, dformat)
        aware_date = pytz.utc.localize(unaware_date_object)
        return aware_date


    def get_json(self):
        token = settings.GITHUB_TOKEN
        url = "https://api.github.com/user/repos?access_token={}".format(token)
        data = urlopen(url).read()
        return json.loads(data)

