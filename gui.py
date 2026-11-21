import os
import sys
import subprocess

# ==============================================================================
# 🔥 NATHAN FELIX LIVE BRIDGE - ROOT GUI LAUNCHER v3.0 🔥
# ==============================================================================

def auto_install_deps():
    required = [("customtkinter", "customtkinter"), ("pillow", "PIL"), ("paramiko", "paramiko")]
    missing = []
    for pkg, imp in required:
        try: __import__(imp)
        except ImportError: missing.append(pkg)
    if missing:
        print(f"\n [ 📦 AUTO-INSTALL ] Terdeteksi library belum terinstall: {', '.join(missing)}")
        print(" Sedang menginstall secara otomatis via pip... Mohon tunggu sebentar...\n")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
            print(" [ ✔ INSTALLASI BERHASIL! ] Melanjutkan program...\n")
        except Exception as e:
            print(f" [ ❌ GAGAL ] Harap install manual: pip install {' '.join(missing)}")
            sys.exit(1)

def launch_gui():
    auto_install_deps()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    bridge_dir = os.path.join(root_dir, "felix_bridge")
    
    if bridge_dir not in sys.path:
        sys.path.insert(0, bridge_dir)
        
    try:
        import felix_app
        app = felix_app.FelixEnterpriseApp()
        app.mainloop()
    except Exception as e:
        print(f"\n [❌ ERROR] Gagal memuat felix_bridge/felix_app.py: {e}\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n [ 🛑 ] Aplikasi GUI dimatikan. Sampai jumpa lagi bosqu!\n")
        sys.exit(0)

if __name__ == '__main__':
    launch_gui()
