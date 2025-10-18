import subprocess
import sys

required_packages = [
    "pytest==8.3.0",
    "pytest-bdd==7.2.0",
    "selenium==4.22.0",
    "allure-pytest==2.13.5",
    "PyYAML==6.0",
    "webdriver-manager==4.0.2",
    "setuptools",
    "wheel",
    "packaging"
]


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
    print("Проверка и установка зависимостей проекта...")
    for package in required_packages:
        try:
            __import__(package.split('==')[0])
        except ImportError:
            print(f"Устанавливаем {package}...")
            install(package)
    print("Все зависимости установлены!")


if __name__ == "__main__":
    main()
