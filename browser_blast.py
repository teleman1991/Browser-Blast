import os
import shutil
import winreg

def remove_chrome_extensions():
    print("Removing adware extensions from Chrome...")
    chrome_extensions_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Extensions'
    if os.path.exists(chrome_extensions_path):
        shutil.rmtree(chrome_extensions_path)
        print("Chrome adware extensions removed.")
    else:
        print("No Chrome extensions found.")

def remove_firefox_extensions():
    print("Removing adware extensions from Firefox...")
    firefox_extensions_path = os.path.expanduser('~') + r'\AppData\Roaming\Mozilla\Firefox\Profiles'
    for root, dirs, files in os.walk(firefox_extensions_path):
        for dir in dirs:
            if dir.endswith('.default'):
                extensions_dir = os.path.join(root, dir, 'extensions')
                if os.path.exists(extensions_dir):
                    shutil.rmtree(extensions_dir)
                    print("Firefox adware extensions removed.")
                else:
                    print("No Firefox extensions found.")

def remove_edge_extensions():
    print("Removing adware extensions from Edge...")
    edge_extensions_path = os.path.expanduser('~') + r'\AppData\Local\Microsoft\Edge\User Data\Default\Extensions'
    if os.path.exists(edge_extensions_path):
        shutil.rmtree(edge_extensions_path)
        print("Edge adware extensions removed.")
    else:
        print("No Edge extensions found.")

def main():
    remove_chrome_extensions()
    remove_firefox_extensions() 
    remove_edge_extensions()
    print("Adware removal completed.")

if __name__ == '__main__':
    main()