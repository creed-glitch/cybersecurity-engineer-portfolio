import re
import sys
import os
from collections import defaultdict
from datetime import datetime

# --- Patterns ---
FAILED_PATTERN = r"LOGIN_FAILED user=(\w+) ip=([\d\.]+)"
SUCCESS_PATTERN = r"LOGIN_SUCCESS user=(\w+) ip=([\d\.]+)"
TIMESTAMP_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"

# --- Data Stores ---
failed_timestamps = defaultdict(list)
failed_attempts = defaultdict(int)
ip_targets = defaultdict(set)
admin_success_ips =  set()

# --- Thresholds ---
BRUTE_FORCE_THRESHOLD = 3
TIME_WINDOW_SECONDS = 60
BURST_THRESHOLD = 5

# The brain
def analyze_logs(log_file):

    try:
        with open(log_file, "r") as file:

            for line in file:
                timestamp_match = re.search(TIMESTAMP_PATTERN, line)
                failed_match = re.search(FAILED_PATTERN, line)
                success_match = re.search(SUCCESS_PATTERN, line)

                # --- Failed Logins ---
                if failed_match and timestamp_match:
                    user = failed_match.group(1)
                    ip = failed_match. group(2)
                    timestamp = datetime.strptime(
                        timestamp_match.group(1),
                        "%Y-%m-%d %H:%M:%S"
                    )

                    failed_attempts[(user, ip)] += 1
                    ip_targets[ip].add(user)
                    failed_timestamps[(user,ip)].append(timestamp)

                # --- Successful logins ---
                if success_match:
                    user = success_match.group(1)
                    ip = success_match.group(2)

                    if user == "admin":
                        admin_success_ips.add(ip)

    except FileNotFoundError:
        print("Log file not found.")
        sys.exit()

# --- Burst Detection ---
def detect_bursts(timestamps):
    timestamps.sort()
    busrt_count = 0

    for i in range(len(timestamps)):
        window_start = timestamps[i]
        count = 1

        for j in range(i + 1, len(timestamps)):
            if (timestamps[j] - window_start).total_seconds() <= TIME_WINDOW_SECONDS:
                count += 1
            else:
                break

        if count >= BURST_THRESHOLD:
            burst_count += 1

    return  burst_count


def generate_report(malicious_ips):

    alerts = []

    print("\nSecurity Log  Analysis Report")
    print("-" * 40)
    
    # --- Brute Force + Burst Detection ---
    for (user, ip), count in failed_attempts.items():

        if count >= BRUTE_FORCE_THRESHOLD:
            
            reputation = "Uknown"

            if ip in malicious_ips:
                reputation = "KNOWN MALICIOUS IP"

            alert = f"""
⚠ Possible Brute Force Attack
Target User: {user}
Source IP: {ip}
Failed Attempts: {count}
Threat Intelligence: {reputation}
"""
            alerts.append(alert)
            print(alert)

        # --- Burst detection ---
        bursts = detect_bursts(failed_timestamps[(users, ip)])

        if bursts > 0:
            alert = f"""
symbol Login Burst Detected
Target User: {user}
Source IP: {ip}
Bursts Events: {bursts}
Threshold: {BURST_THRESHOLD} attempts in {TIME_WINDOW_SECONDS} seconds
"""
            alerts.append(alert)
            print(alert)
    
    # --- Multi-user attack ---
    for ip, users in ip_targets.items():
        if len(users) > 2:
            alert = f"""
⚠ Suspicious Activity Detected
Source IP: {ip}
Multiple Accounts Targeted: {len(users)}
"""
            alerts.append(alert)
            print(alert)

    # --- Admin anomaly detection ---
    for ip in admin_success_ips:
        if ip not in malicious_ips:
            continue # u can skip normal IPs if you want strict detection

        alert = f"""
⚠ Suspicious Admin Login Detected
User: admin
Source IP: {ip}
Reason: Login from known malicious IP
"""
        alerts.append(alert)
        print(alert)

    return alerts

def save_report(alerts):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"reports/security_report_{timestamp}.txt"

    with open(report_file, "w") as file:
        file.write("Security Log Analysis Report\n")
        file.write("=" * 40 + "\n")

        for alert in alerts:
            file.write(alert)
            file.write("\n")

    print(f"\nReport saved to {report_file}")


def load_threat_intel():
    malicious_ips = set()

    try:
        with open("threat_intel/malicious_ips.txt", "r") as file:
            for line in file:
                malicious_ips.add(line.strip())

    except FileNotFoundError:
        print("Threat intelligence file not found.")

    return malicious_ips

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit()

    log_file = sys.argv[1]

    analyze_logs(log_file)
    malicious_ips = load_threat_intel()
    alerts = generate_report(malicious_ips)

    if alerts:
        save_report(alerts)
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    main()

