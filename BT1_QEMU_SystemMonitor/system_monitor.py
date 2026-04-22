import psutil
from datetime import datetime
from time import sleep

# Buoc 5 & 6: Mo file log
log_file = open('system_log.txt', 'w')

print("Bat dau giam sat... Nhan Ctrl+C de dung.")

try:
    while True:
        # Buoc 2: Doc CPU (Trung binh cac loi)
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # Buoc 3: Doc RAM (MB) va Disk (%)
        ram = psutil.virtual_memory()
        ram_used = ram.used // (1024**2)
        ram_total = ram.total // (1024**2)
        ram_pct = ram.percent
        
        disk_pct = psutil.disk_usage('/').percent

        # Buoc 7: Logic canh bao 3 muc
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Buoc 4 & 7: Dinh dang dong output
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used}/{ram_total} MB ({ram_pct}%) | Disk: {disk_pct}% | {status}'

        # In ra man hinh
        print(line)
        
        # In canh bao rieng neu khong phai NORMAL
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU dang o {cpu_avg:.1f}%')

        # Buoc 5: Ghi vao file log + flush
        log_file.write(line + '\n')
        log_file.flush()

        # Buoc 4: Lap moi 2 giay
        sleep(2)

except KeyboardInterrupt:
    # Buoc 6: Bat Ctrl+C
    print('\nDung giam sat.')

finally:
    # Buoc 6: Dong file sach se
    log_file.close()
    print('Log saved to system_log.txt')
