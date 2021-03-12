import sys
import psutil

memorymetrics="mem"
cpumetrics="cpu"

cpu=psutil.cpu_times()
vmem=psutil.virtual_memory()
smem=psutil.swap_memory()

if sys.argv[1] == cpumetrics:
    print('system.cpu.idle ' + str(cpu.idle))
    print('system.cpu.nice ' + str(cpu.nice))
    print('system.cpu.system ' + str(cpu.system))
    print('system.cpu.user ' + str(cpu.user))
    print('system.cpu.iowait ' + str(cpu.iowait))
    print('system.cpu.irq ' + str(cpu.irq))
    print('system.cpu.softirq ' + str(cpu.softirq))
    print('system.cpu.steal ' + str(cpu.steal))
    print('system.cpu.guest ' + str(cpu.guest))
    print('system.cpu.guest_nice ' + str(cpu.guest_nice))
elif sys.argv[1] == memorymetrics:
    print('virtual total ' + str(vmem.total))
    print('virtual available ' + str(vmem.available))
    print('virtual percent ' + str(vmem.percent))
    print('virtual used ' + str(vmem.used))
    print('virtual free ' + str(vmem.free))
    print('virtual active ' + str(vmem.active))
    print('virtual inactive ' + str(vmem.inactive))
    print('virtual buffers ' + str(vmem.buffers))
    print('virtual cached ' + str(vmem.cached))
    print('virtual shared ' + str(vmem.shared))
    print('virtual slab ' + str(vmem.slab))
    print('swap total ' + str(smem.total))
    print('swap used ' + str(smem.used))
    print('swap free ' + str(smem.free))
    print('swap percent ' + str(smem.percent))
    print('swap sin ' + str(smem.sin))
    print('swap sout ' + str(smem.sout))
else:
    print("enter single parameter cpu or mem")
