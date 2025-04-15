# ve3_automation
Automation test assignment
# VE3 Automation Testing Framework

This is a Selenium + PyTest automation framework to test key functionalities of the [VE3 Website](https://www.ve3.global/).

## ✅ Features
- Page Object Model (POM)
- Homepage load validation
- Search (valid & invalid)
- Contact form submission (valid & invalid)
- Screenshot on failure
- HTML Report generation

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest HTML

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run Tests

```bash
pytest
```

Or run with HTML Report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Screenshots of failed tests will be saved in `screenshots/`.

## 🗂 Project Structure

ve3_automation/
├── pages/
├── tests/
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
├── README.md

## 📌 Notes
- Ensure Chrome is installed
- Tests rely on current structure of [ve3.global](https://www.ve3.global/)
