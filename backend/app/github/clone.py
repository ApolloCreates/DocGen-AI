from pathlib import Path

from git import Repo

REPO_DIR = Path("data/repos")


class RepositoryCloner:

    def clone(self, url: str) -> Path:

        REPO_DIR.mkdir(parents=True, exist_ok=True)

        repo_name = url.rstrip("/").split("/")[-1].replace(".git", "")

        destination = REPO_DIR / repo_name

        if destination.exists():
            return destination

        Repo.clone_from(url, destination)

        return destination