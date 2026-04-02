#IV модуь модификации реестра
import winreg
paths = ['SYSTEM\CurrentControlSet\Services\VBoxNetAdp',
'SOFTWARE\Oracle\VirtualBox',
'SYSTEM\CurrentControlSet\Services\VBoxDrv']
created_regs=[]
cpu_key = r'HARDWARE\DESCRIPTION\System\CentralProcessor\0'
new_name = 'VBox CPU'
old_name =[]
def mod_registry():
    for p in paths:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, p, 0, winreg.KEY_WRITE) as my_key:
            created_regs.append(p)
            winreg.SetValueEx(my_key,"Version", 0, winreg.REG_SZ, '6.1.0')

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_WRITE) as key:
        oldname, reg_type = winreg.QueryValueEx(key, "ProcessorNameString")
        old_name.append(oldname)
        winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, new_name)

def res_registry():
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, old_name)

    try:
        for k in created_regs:
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, k)
    except: pass