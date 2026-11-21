import sys
import subprocess
import time

# ==============================================================================
# 🔥 NATHAN FELIX LIVE BRIDGE - AUTOMATIC DEPENDENCY INSTALLER & CHECKER 🔥
# ==============================================================================
# This script verifies that all required Python libraries (paramiko, 
# customtkinter, pillow) are installed. If anything is missing, it installs
# them automatically via pip without needing manual terminal commands!
# ==============================================================================

REQUIRED_PACKAGES = [
    ("paramiko", "paramiko", "SSH/SFTP Client for Real-Time Live Sync (< 50ms)"),
    ("customtkinter", "customtkinter", "Luxury Dark & Gold Enterprise GUI Framework"),
    ("pillow", "PIL", "Image Processing for Enterprise Logos & Branding")
]

def print_banner():
    print("\n" + "="*72)
    print("   📦 NATHAN FELIX LIVE BRIDGE — AUTOMATIC DEPENDENCY CHECKER 📦")
    print("     Verifying and installing enterprise libraries for your device...")
    print("="*72 + "\n")

def check_and_install():
    print_banner()
    print(f" [ 🐍 ] Python Environment : {sys.executable}")
    print(f" [ 🐍 ] Python Version     : {sys.version.split()[0]}\n")
    print("-" * 72)
    
    missing_packages = []
    
    for pkg_name, import_name, desc in REQUIRED_PACKAGES:
        print(f" [ ? ] Checking {pkg_name:<14} -> ", end="", flush=True)
        try:
            __import__(import_name)
            print("✔ INSTALLED (Ready)")
        except ImportError:
            print("❌ MISSING")
            missing_packages.append((pkg_name, desc))
            
    print("-" * 72 + "\n")
    
    if not missing_packages:
        print(" [ 🎉 CONGRATULATIONS! ] All required libraries are already installed!")
        print(" You are 100% ready to launch 'gui.cmd' or 'connect.cmd' for live coding!\n")
        return True
        
    print(f" [ ⚠️ DETECTED {len(missing_packages)} MISSING LIBRARIES ] Starting auto-installation...\n")
    for pkg_name, desc in missing_packages:
        print(f"   + Installing {pkg_name}: {desc}...")
        
    print("\n [ ⏳ ] Downloading from PyPI... Please wait a moment...\n")
    
    pkgs_to_install = [pkg[0] for pkg in missing_packages]
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *pkgs_to_install])
        print("\n" + "="*72)
        print(" [ ✔ INSTALLATION SUCCESSFUL!! ] All libraries installed seamlessly!")
        print("="*72 + "\n")
        return True
    except Exception as e:
        print("\n" + "="*72)
        print(f" [ ❌ INSTALLATION FAILED ] Error: {e}")
        print(" Please try installing manually by running this command in your terminal:")
        print(f" pip install {' '.join(pkgs_to_install)}")
        print("="*72 + "\n")
        return False

if __name__ == '__main__':
    check_and_install()
    if sys.platform == "win32":
        input(" Press ENTER to close this window...")
