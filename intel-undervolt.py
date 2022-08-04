from cgitb import text
import os
import tkinter as tk
from tkinter import Grid, messagebox
root = tk.Tk()
root.title('intel-undervolt')

def program():
    os.system('systemctl enable intel-undervolt.service')
    os.system('systemctl enable intel-undervolt.service')
    
    with open('/etc/intel-undervolt.conf','r',encoding = 'utf-8') as toRead:
        lines = toRead.readlines()

    entryList =[cpuVoltage,iGPUVoltage,cpuCacheVoltage]
    try:
        for x in entryList:
            value = int(x.get())
            print(type(value))
        
        lines[9] = "undervolt 0 'CPU' " +cpuCacheVoltage.get()+'\n'
        lines[10] = "undervolt 1 'GPU' "+iGPUVoltage.get()+'\n'
        lines[11] = "undervolt 2 'CPU Cache' "+cpuCacheVoltage.get()+'\n'

        with open('/etc/intel-undervolt.conf','w',encoding = 'utf-8') as toWrite:
            toWrite.writelines(lines)

        messagebox.showinfo(title='info',message='voltage applied')
    except:
        messagebox.showerror(title='ERROR',message='wrong or empty values')
    
cpuText = tk.Label(text='CPU Voltage')
cpuVoltage = tk.Entry()
iGPU = tk.Label(text='iGPU Voltage')
iGPUVoltage = tk.Entry()
cacheVoltage = tk.Label(text='Cache Voltage')
cpuCacheVoltage = tk.Entry()
applyButton = tk.Button(text='Apply',command=program)
cpuText.grid(row=0,column=0)
cpuVoltage.grid(row=0,column=1)
iGPU.grid(row=1,column=0)
iGPUVoltage.grid(row=1,column=1)
cacheVoltage.grid(row=2,column=0)
cpuCacheVoltage.grid(row=2,column=1)
applyButton.grid(row=3,columnspan=2)

root.mainloop()
