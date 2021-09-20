import window
import configManager

def main():
    configManager.load_config()
    window.create_window()


if __name__ == '__main__':
    main()
