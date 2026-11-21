import os
import sys
import subprocess

# ==============================================================================
# 🔥 NATHAN FELIX LIVE BRIDGE - ROOT TERMINAL LAUNCHER v3.0 🔥
# ==============================================================================

def auto_install_deps():
    try:
        import paramiko
    except ImportError:
        print("\n [ 📦 AUTO-INSTALL ] Library 'paramiko' (SSH/SFTP Client) belum terinstall.")
        print(" Sedang menginstall secara otomatis via pip... Mohon tunggu sebentar...\n")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "paramiko"])
            print(" [ ✔ INSTALLASI BERHASIL! ] Melanjutkan program...\n")
        except Exception as e:
            print(f" [ ❌ GAGAL ] Harap install manual: pip install paramiko")
            sys.exit(1)

def launch():
    auto_install_deps()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    bridge_dir = os.path.join(root_dir, "felix_bridge")
    
    if bridge_dir not in sys.path:
        sys.path.insert(0, bridge_dir)
        
    try:
        import felix_terminal
        felix_terminal.main()
    except Exception as e:
        print(f"\n [❌ ERROR] Gagal memuat felix_bridge/felix_terminal.py: {e}\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n [ 🛑 ] Live-Sync dimatikan. Sampai jumpa lagi bosqu!\n")
        sys.exit(0)

if __name__ == '__main__':
    launch()
