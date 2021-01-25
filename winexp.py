import cmdline
import tkinter
import pfparse
import sys

in_prm = cmdline.Cmdline(sys.argv)

if in_prm.number() == 0:
    print('No args! Sorry!')
    exit()

if in_prm.exist('path') is False:
    print('No cfg file! Sorry!')
    exit()

cfg = pfparse.Pfparser(in_prm.get('path'))

print(cfg.get())

win = tkinter.Tk()
win.title(cfg.get('title'))
win.geometry("{}x{}".format(cfg.get('width'), cfg.get('height')))
win.resizable(0, 0)

check_btn   = True
btn_list = []
while check_btn:
    next_btn_num = str(len(btn_list) + 1)
    next_btn_name = 'button_' + next_btn_num
    next_btn_pos_x = 'pos_x_' + next_btn_num
    next_btn_pos_y = 'pos_y_' + next_btn_num
    btn_text = cfg.get(next_btn_name)
    if btn_text != None:
        btn_list.append(tkinter.Button(win, text=btn_text))
        btn_list[int(next_btn_num)-1].place(x=int(cfg.get(next_btn_pos_x)), y=int(cfg.get(next_btn_pos_y)))
    else:
        check_btn = False

win.mainloop()
