"""Build the current portfolio. Legacy versions remain in Git history."""
from projects_page import build as build_projects
from finalize import build

if __name__ == "__main__":
    build_projects()
    build()
