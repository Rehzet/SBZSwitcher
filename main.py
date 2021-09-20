import window
import configManager


def main():
    configManager.check_config_file()
    window.create_window()


if __name__ == '__main__':
    main()
