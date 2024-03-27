from pathlib import Path
from tkinter import *
import tkinter as tk
from Bio.Seq import Seq

#path to images
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#translation process
def translation(mrna_seq):
    mrna = Seq(mrna_seq)
    protein_seq = mrna.translate()
    return protein_seq
def process():
    mRNA_sequence = entry_1.get(1.0, 'end-1c')
    translated_sequence = translation(mRNA_sequence)
    entry_2.configure(state='normal')
    entry_2.delete(1.0, END)
    entry_2.insert(INSERT,translated_sequence)
    entry_2.configure(state='disable')
    return translated_sequence

#transcription process
def transcription(dna_seq):
    dna = Seq(dna_seq)
    rna_seq = dna.transcribe()
    return rna_seq

def t_process():
    dna_sequence = entry_1.get(1.0, 'end-1c')
    transcribed_sequence = transcription(dna_sequence)
    entry_2.configure(state='normal')
    entry_2.delete(1.0, END)
    entry_2.insert(INSERT,transcribed_sequence)
    entry_2.configure(state='disable')
    return transcribed_sequence

#reverse-transcription process
def r_transcription(rna_seq):
    rna = Seq(rna_seq)
    dna_seq = rna.back_transcribe()
    return dna_seq

def rt_process():
    rna_sequence = entry_1.get(1.0, 'end-1c')
    r_transcribed_sequence = r_transcription(rna_sequence)
    entry_2.configure(state='normal')
    entry_2.delete(1.0, END)
    entry_2.insert(INSERT,r_transcribed_sequence)
    entry_2.configure(state='disable')
    return r_transcribed_sequence

#creating complementary strand
def complementary(dna_seq):
    dna = Seq(dna_seq)
    complementary_strand = dna.complement()
    return complementary_strand

def c_process():
    dna_sequence = entry_1.get(1.0, 'end-1c')
    complementary_strand = complementary(dna_sequence)
    entry_2.configure(state='normal')
    entry_2.delete(1.0, END)
    entry_2.insert(INSERT,complementary_strand)
    entry_2.configure(state='disable')
    return complementary_strand

#main
window = Tk()
window.title('TranScript')
window.geometry("1080x550")
window.configure(bg = "#383545")

#widgets
canvas = Canvas(window,bg = "#383545",height = 550,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0,0.0,1080.0,64.0,fill="#CCB6B6",outline="")

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(540.0,275.0,image=entry_image_1)
entry_1 = Text(bd=0,bg="#CCB6B6",fg="#000716",highlightthickness=0)
entry_1.place(x=203.0,y=220.0,width=674.0,height=108.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(539.0,441.0,image=entry_image_2)
entry_2 = Text(bd=0,bg="#CCB6B6",fg="#000716",highlightthickness=0, state=tk.NORMAL)
entry_2.place(x=202.0,y=386.0,width=674.0,height=108.0)

canvas.create_text(71.0,13.0,anchor="nw",text="TranScript",fill="#000000",font=("Inter Bold", 30 * -1))

button_1 = Button(text='R-Transcription',borderwidth=0,highlightthickness=0,command=rt_process,relief="flat", bg='#A19696', activebackground='#686262', font=("Inter SemiBold", 14 * -1))
button_1.place(x=610.0,y=109.0,width=135.0,height=49.0)

button_3 = Button(text='Complementary',borderwidth=0,highlightthickness=0,command=c_process,relief="flat", bg='#A19696', activebackground='#686262', font=("Inter SemiBold", 14 * -1))
button_3.place(x=892.0,y=109.0,width=135.0,height=49.0)

button_2 = Button(text='Transcription',borderwidth=0,highlightthickness=0,command=t_process,relief="flat",bg='#A19696', activebackground='#686262', font=("Inter SemiBold", 14 * -1))
button_2.place(x=329.0,y=108.0,width=135.0,height=49.0)

button_4 = Button(text='Translation',borderwidth=0,highlightthickness=0,command=process,relief="flat",bg='#A19696', activebackground='#686262', font=("Inter SemiBold", 14 * -1))
button_4.place(x=52.0,y=109.0,width=135.0,height=49.0)

canvas.create_text(468.0,193.0,anchor="nw",text="Enter your sequence:",fill="#FFFFFF",font=("Inter SemiBold", 14 * -1))
canvas.create_text(516.0,355.0,anchor="nw",text="Result:",fill="#FFFFFF",font=("Inter SemiBold", 14 * -1))

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(46.0,32.0,image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(119.0,91.0,image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(397.0,91.0,image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(677.0,91.0,image=image_image_4)

#Additional images
image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(958,91,image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(135.0,441.0,image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(7.0,441.0,image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(135.0,441.0,image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(7.0,441.0,image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(50.0,441.0,image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(135.0,275.0,image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(7.0,275.0,image=image_image_12)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(135.0,275.0,image=image_image_13)

image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(7.0,275.0,image=image_image_14)

image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(50.0,275.0,image=image_image_15)

image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(945.0,441.0,image=image_image_16)

image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(1072.0,441.0,image=image_image_17)

image_image_18 = PhotoImage(file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(945.0,441.0,image=image_image_18)

image_image_19 = PhotoImage(file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(1072.0,441.0,image=image_image_19)

image_image_20 = PhotoImage(file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(1030.0,441.0,image=image_image_20)

image_image_21 = PhotoImage(file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(945.0,275.0,image=image_image_21)

image_image_22 = PhotoImage(file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(1072.0,275.0,image=image_image_22)

image_image_23 = PhotoImage(file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(945.0,275.0,image=image_image_23)

image_image_24 = PhotoImage(file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(1072.0,275.0,image=image_image_24)

image_image_25 = PhotoImage(file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(1030.0,275.0,image=image_image_25)
#run
window.resizable(False, False)
window.mainloop()
