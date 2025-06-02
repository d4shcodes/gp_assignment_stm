# Simple Calculator Project

A Python CLI calculator with unit tests, coverage reporting, and mutation testing.

```bash
# 🧪 Run unit tests:
python -m unittest tests/test_main.py -v

# 📊 Run coverage and generate HTML report:
coverage run -m unittest tests/test_main.py -v
coverage html

# 🦠 Mutation testing (Windows PowerShell):
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate
# 🔍 Ensure mutpy is installed:
pip show mutpy
# 🧬 Run mutpy and generate HTML report:
python .\.venv\Scripts\mut.py --target calculator_func.py --unit-test tests.test_main --report-html mutpy_report
