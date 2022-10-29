from subprocess import check_output

while True:

    def process_exists(process_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        processes = []
        for process in check_output(call).splitlines()[3:]:
            process = process.decode()
            processes.append(process.split())
        return processes
        
    enter_process= input("Check process: ")+".exe"

    if process_exists(enter_process):
        print(f"\n{enter_process} is working\n")

    else:
        print(f"\n{enter_process} does not work\n")

