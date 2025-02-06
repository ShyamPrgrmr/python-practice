import os

virtual_env_dir = os.environ.get('VIRTUAL_ENV')

if virtual_env_dir:
    virtual_env_name = os.path.basename(virtual_env_dir)
    print("Current virtual environment:", virtual_env_name)

else:
    print("Not in a virtual environment")