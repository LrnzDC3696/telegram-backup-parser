import os
from margelet import Backup

BACKUP_PATH = os.path.join('backups', 'ChatExport_2023-02-27')


def test_backup():
    backup = Backup.from_folder_path(BACKUP_PATH)
