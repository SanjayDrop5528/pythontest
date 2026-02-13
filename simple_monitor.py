import time
import subprocess
import urllib.request
import urllib.error
import os
import signal
from datetime import datetime

class SimpleHealthMonitor:
    def __init__(self):
        self.app_script = "app.py"
        self.health_url = "http://localhost:5000/"
        self.check_interval = 10
        self.process = None
        self.restart_count = 0
    
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def start_app(self):
        try:
            self.log(f"Starting {self.app_script}...")
            self.process = subprocess.Popen(
                ["python3", self.app_script],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            time.sleep(5)
            self.log(f"App started with PID: {self.process.pid}")
            return True
        except Exception as e:
            self.log(f"Failed to start: {e}")
            return False
    
    def stop_app(self):
        if self.process:
            try:
                self.log("Stopping app...")
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                self.process.kill()
    
    def is_running(self):
        if self.process is None:
            return False
        return self.process.poll() is None
    
    def check_health(self):
        try:
            response = urllib.request.urlopen(self.health_url, timeout=5)
            return response.status == 200
        except:
            return False
    
    def restart_app(self):
        self.log("Restarting app...")
        self.stop_app()
        time.sleep(2)
        if self.start_app():
            self.restart_count += 1
            self.log(f"Restarted (Total: {self.restart_count})")
            return True
        return False
    
    def monitor(self):
        self.log("=== Monitor Started ===")
        
        if not self.start_app():
            return
        
        failures = 0
        
        while True:
            try:
                time.sleep(self.check_interval)
                
                if not self.is_running() or not self.check_health():
                    failures += 1
                    self.log(f"Health check failed ({failures}/3)")
                    
                    if failures >= 3:
                        self.restart_app()
                        failures = 0
                else:
                    failures = 0
                
            except KeyboardInterrupt:
                self.log("Stopped by user")
                self.stop_app()
                break

if __name__ == "__main__":
    monitor = SimpleHealthMonitor()
    monitor.monitor()
