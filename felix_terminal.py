import paramiko
import os
import time
import json
import sys
import socket
import threading

# ==============================================================================
# ðŸ”¥ NATHAN FELIX LIVE BRIDGE - TERMINAL ENTERPRISE EDITION v3.0 ðŸ”¥
# ==============================================================================
# Created by Nathan Felix (Zero GUI / Zero Exe / Zero Defender Blocks!)
# ==============================================================================

CONFIG_FILE = "felix_config.json"
VALID_LICENSE_KEYS = ["FELIX-VIP-2026", "NATHAN-FELIX-PRO", "FELIX-ELITE", "ASHLEYFELICIA"]
ADMIN_NETWORK_PREFIXES = ["10.247.", "100.", "192.168.", "172.", "10.", "127."]

def get_project_root():
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "resources")) or os.path.exists(os.path.join(cwd, "app")):
        return cwd
    parent = os.path.dirname(cwd)
    if os.path.exists(os.path.join(parent, "resources")) or os.path.join(parent, "app")):
        return parent
    return cwd

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def print_banner():
    print("\n" + "="*72)
    print("   _   _       _   _                     _____     _ _")
    print("  | \\ | |     | | | |                   |  ___|   | (_)")
    print("  |  \\| | __ _| |_| |__   __ _ _ __     | |_ / _ \\| |_|_ _ __")
    print("  | . ` |/ _` | __| '_ \\ / _` | '_ \\    |  _|  __/| | | \\ \\ / /")
    print("  |_|\\_|\\__,_|\\__|_| |_|\\__,_|_| |_|   |_|  \\___||_|_|_/_\\_\\")
    print("     ðŸ”¥ NATHAN FELIX LIVE BRIDGE â€” ENTERPRISE EDITION v3.0 ðŸ”¥")
    print("    (Zero Defender Blocks / Real-Time SFTP / Command Library)")
    print("="*72 + "\n")

def find_active_ip(config):
    candidate_ips = ["YOUR_SERVER_IP", "192.168.1.100", "100.x.x.x"]
    saved_host = config.get("host")
    if saved_host and saved_host not in candidate_ips:
        candidate_ips.insert(0, saved_host)
        
    for ip in candidate_ips:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            res = s.connect_ex((ip, 22))
            s.close()
            if res == 0:
                return ip
        except:
            pass
    return saved_host if saved_host else candidate_ips[0]

def verify_license(config):
    pass

def setup_wizard(config_path):
    print_banner()
    print(" [âš™ï¸ SETUP & RECONFIGURATION] Konfigurasi Koneksi Server...\n")
    
    current_ip = get_local_ip()
    print(f" [ðŸŒ NETWORK CHECK] IP Jaringan Lokal Anda: {current_ip}\n")
    
    ip = input(" [?] Masukkan IP Server Linux Ubuntu [default auto-discover]: ").strip()
    if not ip:
        ip = "YOUR_SERVER_IP"
        
    user = input(" [?] Masukkan Username Linux [default: felixss]: ").strip()
    if not user:
        user = "felixss"
        
    pwd = input(" [?] Masukkan Password Linux [default: felixs]: ").strip()
    if not pwd:
        pwd = ""
        
    path = input(" [?] Masukkan Remote Web Folder [default: /var/www/corporat]: ").strip()
    if not path:
        path = "/var/www/corporat"
        
    config = {
        "host": ip,
        "username": user,
        "password": pwd,
        "remote_root": path
    }
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
        
    print("\n [âœ” KONFIGURASI TERSIMPAN!!] Melanjutkan koneksi ke server...\n")
    return config

def load_config(config_path):
    if "--reset" in sys.argv or "-r" in sys.argv:
        return setup_wizard(config_path)
        
    config = {
        "username": "felixss",
        "password": "",
        "remote_root": "/var/www/corporat",
        "host": "YOUR_SERVER_IP"
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                saved_config = json.load(f)
                config.update(saved_config)
        except Exception as e:
            pass
            
    active_ip = find_active_ip(config)
    config["host"] = active_ip
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except:
        pass
        
    return config

def live_sync_worker(config, stop_event):
    local_root = get_project_root()
    remote_root = config["remote_root"]
    watch_folders = ["app", "resources", "routes", "config", "public", "database"]
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sftp = None
    connected = False
    
    mtimes = {}
    for folder in watch_folders:
        folder_path = os.path.join(local_root, folder)
        for root_dir, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(('.php', '.blade.php', '.css', '.js', '.json', '.env', '.md')):
                    full_path = os.path.join(root_dir, file)
                    try:
                        mtimes[full_path] = os.stat(full_path).st_mtime
                    except:
                        pass

    while not stop_event.is_set():
        time.sleep(0.5)
        if not connected or sftp is None:
            try:
                ssh.connect(config['host'], username=config['username'], password=config['password'], timeout=5)
                sftp = ssh.open_sftp()
                connected = True
                print(f"\n [ ðŸŸ¢ LIVE BRIDGE CONNECTED ] -> SFTP tunnel aktif ke {config['username']}@{config['host']}!")
                print(" [ # ] NATHAN FELIX BRIDGE READY!! SIAP LIVE CODING!!")
                print(" [ > ] Ketik 'menu' untuk melihat daftar perintah cepat Laravel/Linux.\n")
                print(f" ðŸ’» {config['username']}@remote:~$ ", end="", flush=True)
            except:
                connected = False
                sftp = None
                time.sleep(3.0)
                continue

        for folder in watch_folders:
            folder_path = os.path.join(local_root, folder)
            for root_dir, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(('.php', '.blade.php', '.css', '.js', '.json', '.env', '.md')):
                        full_path = os.path.join(root_dir, file)
                        try:
                            current_mtime = os.stat(full_path).st_mtime
                            if full_path not in mtimes:
                                mtimes[full_path] = current_mtime
                            elif current_mtime > mtimes[full_path]:
                                mtimes[full_path] = current_mtime
                                
                                rel_path = os.path.relpath(full_path, local_root).replace("\\", "/")
                                remote_path = f"{remote_root}/{rel_path}"
                                
                                print(f"\n [ >>> TERDETEKSI EDIT ] Syncing: {rel_path}...")
                                start_t = time.time()
                                
                                remote_dir = os.path.dirname(remote_path)
                                try:
                                    sftp.stat(remote_dir)
                                except:
                                    ssh.exec_command(f"echo {config['password']} | sudo -S mkdir -p {remote_dir} && echo {config['password']} | sudo -S chown -R {config['username']}:www-data {remote_dir} && echo {config['password']} | sudo -S chmod -R 775 {remote_dir}")
                                    time.sleep(0.5)
                                    
                                try:
                                    sftp.put(full_path, remote_path)
                                    elapsed = round(time.time() - start_t, 2)
                                    print(f" [ *** DAH KESIMPAN AMAN!! *** ] -> {remote_path} ({elapsed}s)")
                                    print(f" ðŸ’» {config['username']}@remote:~$ ", end="", flush=True)
                                except Exception as put_err:
                                    print(f" [ !!! SYNC ERROR !!! ] Gagal upload: {put_err}")
                                    print(" [ ! ] Mencoba perbaikan izin akses folder otomatis via sudo chown...")
                                    try:
                                        ssh.exec_command(f"echo {config['password']} | sudo -S chown -R {config['username']}:www-data {remote_root} && echo {config['password']} | sudo -S chmod -R 775 {remote_root}")
                                        time.sleep(1.0)
                                        sftp.put(full_path, remote_path)
                                        print(f" [ *** SYNC SUKSES *** ] -> {remote_path} (AUTO-RETRY BERHASIL!)")
                                        print(f" ðŸ’» {config['username']}@remote:~$ ", end="", flush=True)
                                    except Exception as e2:
                                        print(f" [ âŒ ] Retry gagal: {e2}")
                                        connected = False
                                        sftp = None
                        except:
                            pass

    if sftp: sftp.close()
    if ssh: ssh.close()

def exec_ssh(config, cmd_text):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(config['host'], username=config['username'], password=config['password'], timeout=6)
        remote_root = config["remote_root"]
        
        if cmd_text.startswith("sudo "):
            real_cmd = f"cd {remote_root} && echo {config['password']} | sudo -S {cmd_text[5:]} 2>&1"
        else:
            real_cmd = f"cd {remote_root} && {cmd_text} 2>&1"
            
        _, stdout, _ = ssh.exec_command(real_cmd)
        output = stdout.read().decode('utf-8', errors='replace').strip()
        ssh.close()
        
        print("\n" + "-"*72)
        if output:
            for line in output.split("\n"):
                print(f"   {line}")
        else:
            print("   [ âœ” Perintah berhasil dieksekusi (Tidak ada output) ]")
        print("-" * 72)
    except Exception as e:
        print(f"\n [ âŒ SSH EXEC ERROR ] -> {e}\n")

def print_menu():
    print("\n" + "="*72)
    print(" ðŸ“š NATHAN FELIX COMMAND LIBRARY - DAFTAR PERINTAH CEPAT")
    print("="*72)
    print(" [ 1 ] ðŸ§¹ Laravel: Clear All Cache (optimize:clear)")
    print(" [ 2 ] ðŸ—„ï¸  Laravel: Check DB Migrations Status")
    print(" [ 3 ] ðŸš€ Laravel: Run Migrations (migrate --force)")
    print(" [ 4 ] ðŸŒ± Laravel: Seed Database (db:seed --force)")
    print(" [ 5 ] ðŸ› ï¸  Laravel: Toggle Maintenance Mode (php artisan down/up)")
    print(" [ 6 ] ðŸŒ Tailscale: Enable Public Funnel (Port 80)")
    print(" [ 7 ] ðŸ›‘ Tailscale: Check Funnel Status")
    print(" [ 8 ] ðŸ“œ Linux: View Laravel Error Log (Last 20 Lines)")
    print(" [ 9 ] ðŸ”‘ Linux: Fix File Permissions (chown www-data)")
    print(" [ 10] ðŸ“Š Linux: Check Server Uptime, CPU & RAM Usage")
    print(" [ r ] ðŸ”„ Reconfigure Connection (Reset felix_config.json)")
    print(" [ q ] ðŸ›‘ Keluar & Matikan Live-Sync")
    print("="*72)
    print(" * Tips: Anda juga bisa langsung mengetik perintah Linux manual di prompt!")
    print("="*72 + "\n")

def main():
    print_banner()
    project_root = get_project_root()
    config_path = os.path.join(project_root, "felix_bridge", CONFIG_FILE)
    if not os.path.exists(os.path.dirname(config_path)):
        config_path = os.path.join(project_root, CONFIG_FILE)
        
    config = load_config(config_path)
    
    print(f" [ ðŸ“ ] Workspace Root : {project_root}")
    print(f" [ ðŸŒ ] Target Server  : {config['username']}@{config['host']} ({config['remote_root']})")
    print(" [ âš¡ ] Memulai background Live-Sync Tunnel...")
    
    stop_event = threading.Event()
    sync_thread = threading.Thread(target=live_sync_worker, args=(config, stop_event), daemon=True)
    sync_thread.start()
    
    time.sleep(1.5)
    
    try:
        while True:
            cmd = input(f" ðŸ’» {config['username']}@remote:~$ ").strip()
            if not cmd:
                continue
            if cmd.lower() in ['q', 'quit', 'exit']:
                print("\n [ ðŸ›‘ ] Mematikan Nathan Felix Live Bridge... Sampai jumpa lagi bosqu!\n")
                break
            elif cmd.lower() in ['menu', 'help', '?']:
                print_menu()
            elif cmd == '1':
                exec_ssh(config, "php artisan optimize:clear")
            elif cmd == '2':
                exec_ssh(config, "php artisan migrate:status")
            elif cmd == '3':
                exec_ssh(config, "php artisan migrate --force")
            elif cmd == '4':
                exec_ssh(config, "php artisan db:seed --force")
            elif cmd == '5':
                print(" [ ðŸ› ï¸ ] Memeriksa status Maintenance Mode...")
                exec_ssh(config, "if [ -f storage/framework/down ]; then sudo php artisan up; echo 'ðŸŸ¢ SITUS KEMBALI ONLINE!'; else sudo php artisan down --secret='maintenance-secret'; echo 'âš ï¸ SITUS MASUK MAINTENANCE MODE (Bypass: /maintenance-secret)'; fi")
            elif cmd == '6':
                exec_ssh(config, "sudo tailscale funnel --bg 80")
            elif cmd == '7':
                exec_ssh(config, "sudo tailscale funnel status")
            elif cmd == '8':
                exec_ssh(config, "tail -n 20 storage/logs/laravel.log")
            elif cmd == '9':
                exec_ssh(config, f"sudo chown -R {config['username']}:www-data . && sudo chmod -R 775 .")
            elif cmd == '10':
                exec_ssh(config, "uptime && free -m && df -h")
            elif cmd.lower() == 'r':
                print("\n [ ðŸ”„ ] Me-reset konfigurasi...")
                stop_event.set()
                time.sleep(0.5)
                config = setup_wizard(config_path)
                stop_event.clear()
                sync_thread = threading.Thread(target=live_sync_worker, args=(config, stop_event), daemon=True)
                sync_thread.start()
            else:
                exec_ssh(config, cmd)
    except KeyboardInterrupt:
        print("\n\n [ ðŸ›‘ ] Live-Sync dimatikan via Ctrl+C. Sampai jumpa lagi bosqu!\n")
    finally:
        stop_event.set()

if __name__ == '__main__':
    main()

