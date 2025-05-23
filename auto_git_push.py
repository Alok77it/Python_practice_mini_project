import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Your actual local repo path
REPO_PATH = "/home/nobroker/Downloads/Python_practice_mini_project"

class GitAutoPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print(f"🔄 Change detected: {event.src_path}")
        self.git_push()

    def git_push(self):
        try:
            # Stage all changes
            subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)

            # Commit with a timestamp
            commit_message = f"Auto commit at {time.strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_message], cwd=REPO_PATH, check=True)

            # Push to the remote repo
            subprocess.run(["git", "push"], cwd=REPO_PATH, check=True)

            print(f"✅ Changes pushed: {commit_message}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")

if __name__ == "__main__":
    print(f"📂 Watching for changes in: {REPO_PATH}")
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
