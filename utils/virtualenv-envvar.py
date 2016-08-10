#!/usr/bin/env python
"""
This script helps set virtualenv-specific environment variables.
The variables are set in the script hook and are removed in the
script hook of the virtualenv.

SETUP
- Make sure that this file is executable :
    chmod +x /path/to/this/script
- Set an alias in ~/.bashrc :
    alias virtualenv-envvar="/path/to/this/script"

USAGE
- Activate the desired virtualenv.
- Change directory to the python project related to the virtualenv (this will
affect default values).
"""
import os
import argparse


def main(django_settings_module=False):

    try:
        VENV_DIR = os.environ['VIRTUAL_ENV']
        VENV_NAME = os.path.basename(VENV_DIR)
        ACTIVATE_THIS_FILE = os.path.join(VENV_DIR, 'bin/activate_this.py')
        POSTACTIVATE_FILE = os.path.join(VENV_DIR, 'bin/postactivate')
        POSTDEACTIVATE_FILE = os.path.join(VENV_DIR, 'bin/postdeactivate')
    except KeyError as e:
        print('No virtualenv activated.')
        return

    print('This utility will walk you through configuring environment '
          'variables for the virtualenv ({}).\n'
          'It only covers PYTHONPATH and DJANGO_SETTINGS_MODULE, and tries to '
          'guess sensible defaults.\n\n'
          'Press ^C at any time to quit.'
          .format(VENV_NAME))

    WORKING_DIR = os.getcwd()
    PROJECT_DIR = ''
    DJANGO_SETTINGS_MODULE = 'config.settings.local'

    # 1. Get environment variables
    while not os.path.exists(PROJECT_DIR):
        if PROJECT_DIR != '':
            print('The following directory does not exist: {}\n'
                  .format(PROJECT_DIR))
        else:
            PROJECT_DIR = os.getcwd()

        response = raw_input('PYTHONPATH: ({}) '.format(WORKING_DIR))
        if response == '':
            PROJECT_DIR = WORKING_DIR
        else:
            PROJECT_DIR = response

    if django_settings_module:
        response = raw_input('DJANGO_SETTINGS_MODULE: ({}) '
                             .format(DJANGO_SETTINGS_MODULE))
        if response == '':
            DJANGO_SETTINGS_MODULE = DJANGO_SETTINGS_MODULE
        else:
            DJANGO_SETTINGS_MODULE = response

    # 2. Set environment variables

    ## postactivate hook
    script = "#!/bin/bash\n"
    script += "# This hook is sourced after this virtualenv is activated.\n\n"
    script += "export PYTHONPATH={}:$PYTHONPATH\n".format(PROJECT_DIR)
    if django_settings_module:
        script += "export DJANGO_SETTINGS_MODULE={}".format(DJANGO_SETTINGS_MODULE)

    print('About to write to {}:\n\n{}\n\n'.format(POSTACTIVATE_FILE, script))
    response = raw_input('Is this ok? (yes) ')
    if response == '' or response == 'yes':
        with open(POSTACTIVATE_FILE, mode='w') as f:
            f.write(script)
    else:
        print('Exiting utility.')
        return

    ## postdeactivate hook
    script = "#!/bin/bash\n"
    script += "# This hook is sourced after this virtualenv is deactivated.\n\n"
    script += "export PYTHONPATH=${{PYTHONPATH#{}:}}\n".format(PROJECT_DIR)
    if django_settings_module:
        script += "unset DJANGO_SETTINGS_MODULE"

    with open(POSTDEACTIVATE_FILE, mode='w') as f:
        f.write(script)

    # 3. Re-activate virtualenv
    execfile(ACTIVATE_THIS_FILE, dict(__file__=ACTIVATE_THIS_FILE))
    # os.system("{}/bin/activate".format(VENV_DIR))


    print('\nThank you. The environment variables have been configured for '
          'the virtualenv: {}'.format(VENV_NAME))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--django', action='store_true',
                        help='Enable DJANGO_SETTINGS_MODULE')
    args = parser.parse_args()

    main(django_settings_module=args.django)
