import time
import subprocess
import requests
import psutil
import os
import signal
from datetime import datetime

class AppHealthMonitor:
    def __init__(self, app_script="app.py", host="localhost", port=5000, check_interval=10):
        self.app_script = app_script
        self.host = host
        self.port = port
        self.check_interval = check_interval
        self.health_url = f"http://{host}:{port}/"
        self.process = None
        self.restart_count = 0
        self.log_file = "health_monitor.log"
    
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(self.log_file, 'a') as f:
            f.write(log_message + "\n")
    
    def start_app(self):
        try:
            self.log(f"Starting {self.app_script}...")
            self.process = subprocess.Popen(
                ["python", self.app_script],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )
            time.sleep(3)
            self.log(f"App started with PID: {self.process.pid}")
            return True
        except Exception as e:
            self.log(f"Failed to start app: {e}")
            return False
    
    def stop_app(self):
        if self.process:
            try:
                self.log(f"Stopping app (PID: {self.process.pid})...")
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
                self.process.wait(timeout=5)
                self.log("App stopped successfully")
            except Exception as e:
                self.log(f"Error stopping app: {e}")
                try:
                    os.killpg(os.getpgid(self.process.pid), signal.SIGKILL)
                except:
                    pass
    
    def is_process_running(self):
        if self.process is None:
            return False
        
        try:
            process = psutil.Process(self.process.pid)
            return process.is_running() and process.status() != psutil.STATUS_ZOMBIE
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
    
    def check_health(self):
        try:
            response = requests.get(self.health_url, timeout=5)
            if response.status_code == 200:
                return True
            else:
                self.log(f"Health check failed: HTTP {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            self.log(f"Health check failed: {e}")
            return False
    
    def restart_app(self):
        self.log("Restarting app...")
        self.stop_app()
        time.sleep(2)
        if self.start_app():
            self.restart_count += 1
            self.log(f"App restarted successfully (Total restarts: {self.restart_count})")
            return True
        else:
            self.log("Failed to restart app")
            return False
    
    def monitor(self):
        self.log("=== Health Monitor Started ===")
        
        if not self.start_app():
            self.log("Failed to start app initially. Exiting.")
            return
        
        consecutive_failures = 0
        max_consecutive_failures = 3
        
        while True:
            try:
                time.sleep(self.check_interval)
                
                process_running = self.is_process_running()
                health_ok = self.check_health()
                
                if not process_running:
                    self.log("Process not running!")
                    consecutive_failures += 1
                elif not health_ok:
                    self.log("Health check failed!")
                    consecutive_failures += 1
                else:
                    if consecutive_failures > 0:
                        self.log("Health check passed")
                    consecutive_failures = 0
                    continue
                
                if consecutive_failures >= max_consecutive_failures:
                    self.log(f"Max failures reached ({consecutive_failures}). Restarting...")
                    if self.restart_app():
                        consecutive_failures = 0
                    else:
                        self.log("Restart failed. Waiting before retry...")
                        time.sleep(30)
                
            except KeyboardInterrupt:
                self.log("Monitor stopped by user")
                self.stop_app()
                break
            except Exception as e:
                self.log(f"Monitor error: {e}")
                time.sleep(5)

if __name__ == "__main__":
    monitor = AppHealthMonitor(
        app_script="app.py",
        host="localhost",
        port=5000,
        check_interval=10
    )
    monitor.monitor()
