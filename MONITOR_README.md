# Health Monitor for app.py

## Overview
Automatically monitors and restarts the Flask application if it stops or becomes unhealthy.

## Features
- Process monitoring
- HTTP health checks
- Automatic restart on failure
- Logging with timestamps
- Configurable check intervals
- Graceful shutdown handling

## Files

### health_monitor.py (Full-featured)
- Uses psutil for advanced process monitoring
- Detailed health checks
- Comprehensive logging
- Configurable parameters

### simple_monitor.py (Lightweight)
- Uses only standard library
- Basic health checks
- Minimal dependencies
- Easy to deploy

## Installation

```bash
# For full-featured monitor
pip install -r requirements_monitor.txt

# For simple monitor (no extra dependencies needed)
# Just use Python 3 standard library
```

## Usage

### Option 1: Full-featured Monitor
```bash
python health_monitor.py
```

### Option 2: Simple Monitor
```bash
python simple_monitor.py
```

### Run in Background
```bash
# Linux/Mac
nohup python health_monitor.py > monitor.log 2>&1 &

# Or use screen
screen -dmS monitor python health_monitor.py
```

## Configuration

Edit the monitor script to customize:

```python
monitor = AppHealthMonitor(
    app_script="app.py",      # Script to monitor
    host="localhost",          # App host
    port=5000,                 # App port
    check_interval=10          # Check every 10 seconds
)
```

## How It Works

1. **Start**: Launches app.py as subprocess
2. **Monitor**: Checks every 10 seconds:
   - Is process running?
   - Does HTTP health check pass?
3. **Detect**: Counts consecutive failures
4. **Restart**: After 3 failures, restarts the app
5. **Log**: Records all events with timestamps

## Health Check Logic

```
Every 10 seconds:
├── Check if process is running
├── Check if HTTP endpoint responds
├── If both OK: Reset failure counter
└── If either fails:
    ├── Increment failure counter
    └── If failures >= 3:
        ├── Stop app
        ├── Wait 2 seconds
        └── Start app
```

## Logs

Monitor creates `health_monitor.log` with entries like:
```
[2024-01-15 10:30:00] === Health Monitor Started ===
[2024-01-15 10:30:00] Starting app.py...
[2024-01-15 10:30:03] App started with PID: 12345
[2024-01-15 10:35:10] Health check failed!
[2024-01-15 10:35:30] Max failures reached (3). Restarting...
[2024-01-15 10:35:35] App restarted successfully (Total restarts: 1)
```

## Stop Monitor

Press `Ctrl+C` to gracefully stop the monitor and the app.

## Production Deployment

For production, consider using:
- **systemd** (Linux)
- **supervisor** (Cross-platform)
- **PM2** (Node.js-based process manager)
- **Docker** with restart policies

### Example systemd service:
```ini
[Unit]
Description=App Health Monitor
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/pythontest
ExecStart=/usr/bin/python3 health_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Troubleshooting

**Monitor can't start app:**
- Check if app.py exists
- Verify Python path
- Check file permissions

**Health checks always fail:**
- Verify port 5000 is not in use
- Check firewall settings
- Ensure Flask dependencies installed

**Too many restarts:**
- Increase check_interval
- Increase max_consecutive_failures
- Check app.py for errors
