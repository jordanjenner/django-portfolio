from django.apps import AppConfig
from projects.models import Project
from datetime import datetime
import pytz
import re
from django.conf import settings
import json
from urllib.request import Request, urlopen


class SchedulerConfig(AppConfig):
    name = 'scheduler'


class RepoPuller():
    def __init__(self):
        self.repos = self.get_json()
        self.import_data()

    def import_data(self):
        repo_ids = []

        for repo in self.repos:
            if repo["owner"]["login"] == "jordanjenner":
                repo_id = repo["id"]
                title = None
                name = repo["name"]
                repo_ids.append(repo_id)
                url = repo["svn_url"]
                creation_date = repo["created_at"]
                creation_date = self.date_convert(creation_date)
                last_updated = repo["updated_at"]
                last_updated = self.date_convert(last_updated)
                description = repo["description"]
                language = repo["language"]
                is_private = repo["private"]
                is_live = False
                live_url = None
                size = int(repo["size"])

                readme = self.get_readme(repo["owner"]["login"], name)

                for line in readme.split('\n'):
                    if line.startswith('#'):
                        title = line[1:].strip()
                    if line.startswith('Live:'):
                        print(line)
                        is_live = True
                        live_url = re.split("\(|\)", line)[1]
                        print(live_url)



                try:
                    project = Project.objects.get(repo_id=repo_id)

                    project.repo_id = repo_id
                    project.repo_url = url
                    project.title = title
                    project.name = name
                    project.creation_date = creation_date
                    project.last_updated = last_updated
                    project.description = description
                    project.language = language
                    project.is_private = is_private
                    project.size = size
                    project.is_live = is_live
                    project.live_url = live_url

                    project.save()

                except Project.DoesNotExist:
                    Project.objects.create(
                        repo_id=repo_id,
                        repo_url=url,
                        name=name,
                        title=title,
                        creation_date=creation_date,
                        last_updated=last_updated,
                        description=description,
                        language=language,
                        is_private=is_private,
                        size=size,
                        is_live=is_live,
                        live_url=live_url,
                        )
        
        to_delete = Project.objects.exclude(repo_id__in=repo_ids)

        for project in to_delete:
            project.delete()

    def date_convert(self, strdate):
        dformat = "%Y-%m-%dT%H:%M:%SZ"
        unaware_date_object = datetime.strptime(strdate, dformat)
        aware_date = pytz.utc.localize(unaware_date_object)
        return aware_date

    def get_readme(self, user, repo):
        token = settings.GITHUB_TOKEN
        url = f"https://raw.githubusercontent.com/{user}/{repo}/master/README.md"
        req = Request(url)
        req.add_header('Authorization', 'token {}'.format(token))
        try:
            data = urlopen(req)
        except:
            return ""
        content = data.read().decode(data.headers.get_content_charset())
        return content

    def get_json(self):
        token = settings.GITHUB_TOKEN
        url = "https://api.github.com/user/repos"
        req = Request(url)
        req.add_header('Authorization', 'token {}'.format(token))
        data = urlopen(req).read()
        return json.loads(data)

