import os
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

def program():
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
    

cpuVoltage = tk.Entry()
iGPUVoltage = tk.Entry()
cpuCacheVoltage = tk.Entry()
applyButton = tk.Button(text='Apply',command=program)
cpuVoltage.pack()
iGPUVoltage.pack()
cpuCacheVoltage.pack()
applyButton.pack()


root.mainloop()
