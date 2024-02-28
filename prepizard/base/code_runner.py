import os
import django
from django.conf import settings

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prepizard.settings')
django.setup()

def read_input_file():
    # Path to the input file in the static directory
    file_name = 'input1.txt'
    file_path = os.path.join(settings.STATICFILES_DIRS[0], file_name)

    print("File path:", file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the contents of the file
        with open(file_path, 'r') as file:
            file_content = file.read()
            print("File content:", file_content)
    else:
        # Handle the case where the file does not exist
        print("File not found")

read_input_file()
