import shutil
import datetime
import os

def backup(source, destination):
    # Use datetime.now() to get the current date and time
    backupfile = os.path.join(destination, f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
    
    # Create the backup archive
    shutil.make_archive(backupfile, 'gztar', source)

# Use raw strings for Windows paths
backup(r'C:\Users\Kush\OneDrive\Desktop\DevOps2024\Python', r'C:\Users\Kush\OneDrive\Desktop\DevOps2024\Linux')
