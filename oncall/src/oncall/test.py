import psutil

def find_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None




def get_process_info(pid):
    try:
        process = psutil.Process(pid)
        memory_info = process.memory_info()
        cpu_percent = process.cpu_percent(interval=5) 
        return {
            'pid': pid,
            'memory_usage': memory_info.rss, 
            'cpu_percent': cpu_percent  
        }
    except psutil.NoSuchProcess as e:
        return None



process_name_to_find = "firefox"
pid = find_process_by_name(process_name_to_find)

if pid:
    process_info = get_process_info(pid)
    
    if process_info != None:



