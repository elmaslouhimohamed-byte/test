
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install pytest

- name: Check project files
  run: |
    pwd
    ls -la
    find . -maxdepth 3 -type f

- name: Run application tests
  run: |
    python -m pytest -v tests/
