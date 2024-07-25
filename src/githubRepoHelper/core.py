import os
import stat
import subprocess
import configparser

class GitHubRepositoryHelper:
    CONFIG_PATH = os.path.expanduser("~/.gitrepohelper/config.cfg")
    REPOS_PATH = os.path.expanduser("~/git-repos")

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.github_token = None
        self.initialized = False
        self.initialize()

    def initialize(self):
        if os.path.exists(self.CONFIG_PATH):
            self.initialized = True
            self.load_config()
        else:
            self.setup_initial_configuration()

        if not self.check_gh_cli_installed():
            self.prompt_for_github_token()
        
        self.initialized = True

    def setup_initial_configuration(self):
        os.makedirs(os.path.dirname(self.CONFIG_PATH), exist_ok=True)
        os.makedirs(self.REPOS_PATH, exist_ok=True)
        
        self.config['DEFAULT'] = {
            'repos_path': self.REPOS_PATH
        }
        with open(self.CONFIG_PATH, 'w') as configfile:
            self.config.write(configfile)

        os.chmod(self.CONFIG_PATH, stat.S_IRUSR | stat.S_IWUSR)

    def load_config(self):
        self.config.read(self.CONFIG_PATH)

    def check_gh_cli_installed(self):
        try:
            subprocess.run(['gh', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.CalledProcessError, Fi
