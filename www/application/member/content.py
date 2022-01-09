import os
from flask import current_app

app = current_app


def get_content(user):
    """Get user content"""

    # check directory
    target_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], user.name)
    if os.path.exists(target_path):
        files = os.listdir(target_path)
        return files
    pass
