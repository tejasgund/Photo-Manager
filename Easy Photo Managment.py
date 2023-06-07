try:
    import tkinter as tk
    from tkinter import ttk
    import os
    from PIL import ImageTk, Image
    from tkinter import filedialog
    from tkinter import messagebox
    # from pync import Notifier
    import shutil


    class Images(tk.Tk):
        def __init__(self):
            super().__init__()
            # Notifier.notify("Welcome")
            self.geometry("1920x1800")
            self.configure(bg='black')
            self.title("Gallery")
            self.totalimages = 0
            self.animationvariable = 0
            self.animationvariable1 = 0
            self.animationvariable3 = 200
            # POTRAIT
            self.patrait_setwidth = 420
            self.patrait_setheight = 654
            # LANDSCAPE
            self.landscape_setwidth = 1200
            self.landscape_setheight = 628
            self.Scalevariable = tk.StringVar()
            self.adress = tk.StringVar()
            self.search_number_var = tk.StringVar()
            self.search_text_var = tk.StringVar()
            self.iamagefilename = tk.StringVar()
            self.file_adress = tk.StringVar()

            # statusbar variables
            self.main_file_name = tk.StringVar()
            self.main_folder_name = tk.StringVar()
            self.copy_main_file_name = tk.StringVar()
            self.copy_main_folder_name = tk.StringVar()
            self.active = 0

            self.var = 0

            # ___________________________Creating not Found image
            try:
                self.notfoumdimage = ImageTk.PhotoImage(Image.open("C:\\Users\\vicky\\Pictures\\Camera Roll"))
            except:

                self.notfoumdimage = None

            self.IMAGE = ('ALL',
                          '.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif',
                          '.ppm',
                          '.xbm',
                          '.tiff',
                          '.rgb', '.pgm', '.png', '.pnm', '.JPG')

            # fontS Creating
            font1 = ('didot', 15, 'bold')
            font2 = ("arial", 10, 'bold')
            title = ('phosphate', 15, 'bold')

            # self.adress.set(os.getenv('HOME'))

            self.adress.set('/Users/vicky/Pictures')

            # _______________Creating Main Frame ___________________________________________________________________
            self.frame1 = tk.LabelFrame(self, text='Image', height=750, bg='black', fg='gold', font=title)
            self.frame1.pack(fill=tk.X)
            self.frame2 = tk.LabelFrame(self, text="Slider", height=180, bg='black', fg='gold', font=title)
            self.frame2.pack(fill=tk.X)
            self.frame3 = tk.Label(self, height=10, bg='black', fg='gold')
            self.frame3.pack(fill='both', expand=True, pady=5)

            # ___________________End Main Frame___________________________________________________________________

            # __________________Creating Main Image____________________________
            self.mainphoto = tk.Label(self.frame1, bg='white')
            self.mainphoto.place(relwidth=1, relheight=1)

            # ________________End Main image_________________________________
            # __________________________________________________________________________________MENUBAR
            self.menubar_var = 40
            self.menubar = tk.LabelFrame(self.frame1, text='Menu Bar', bg='skyblue', font=('menio', 15, 'bold'),
                                         fg='black')
            self.menubar.place(width=self.menubar_var, relheight=1)
            self.menubar_collaps_var = 0
            # __________________________________________________________________________________MENUBAR END
            self.w1 = 150
            self.h1 = 150
            # _______________________________Creating Slider Images____________________
            self.image1 = tk.Label(self.frame2, bg='white')
            self.image1.place(x=70, y=1, width=130, height=100)
            self.image2 = tk.Label(self.frame2, bg='white')
            self.image2.place(x=270, y=1, width=self.w1, height=self.h1)
            self.image3 = tk.Label(self.frame2, bg='white')
            self.image3.place(x=470, y=1, width=self.w1, height=self.h1)
            self.image4 = tk.Label(self.frame2, bg='white')
            self.image4.place(x=670, y=1, width=self.w1, height=self.h1)
            self.image5 = tk.Label(self.frame2, bg='white')
            self.image5.place(x=870, y=1, width=self.w1, height=self.h1)
            self.image6 = tk.Label(self.frame2, bg='white')
            self.image6.place(x=1070, y=1, width=self.w1, height=self.h1)
            self.image7 = tk.Label(self.frame2, bg='white')
            self.image7.place(x=1270, y=1, width=self.w1, height=self.h1)

            self.image8 = tk.Label(self.frame2, bg='white')
            self.image8.place(x=1450, y=1, width=350, height=200)

            Name2 = tk.Label(self.image8, textvariable=self.main_file_name)
            Name4 = tk.Label(self.image8, text=self.main_folder_name)
            Name6 = tk.Label(self.image8, textvariable=self.copy_main_folder_name)

            Name2.grid(row=0, column=1, sticky=tk.W, pady=2, padx=5)
            Name4.grid(row=1, column=1, sticky=tk.W, pady=2)
            Name6.grid(row=2, column=1, sticky=tk.W, pady=2)

            self.name1 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name1.place(x=70, y=1)
            self.name2 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name2.place(x=270, y=1)
            self.name3 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name3.place(x=470, y=1)
            self.name4 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name4.place(x=670, y=1)
            self.name5 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name5.place(x=870, y=1)
            self.name6 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name6.place(x=1070, y=1)
            self.name7 = tk.Label(self.frame3, bg='black', wraplength=0, width=10, fg='gold', font=font2)
            self.name7.place(x=1270, y=1)

            self.file1 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file1.place(x=40, y=20)
            self.file2 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file2.place(x=240, y=20)
            self.file3 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file3.place(x=440, y=20)
            self.file4 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file4.place(x=640, y=20)
            self.file5 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file5.place(x=840, y=20)
            self.file6 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file6.place(x=1040, y=20)
            self.file7 = tk.Label(self.frame3, bg='black', wraplength=0, width=20, fg='green', font=font1)
            self.file7.place(x=1240, y=20)

            self.image1.bind("<Button-1>", lambda event: self.animation5(self.var))
            self.image2.bind("<Button-1>", lambda event: self.animation5(self.var + 1))
            self.image3.bind("<Button-1>", lambda event: self.animation5(self.var + 2))
            self.image4.bind("<Button-1>", lambda event: self.animation5(self.var + 3))
            self.image5.bind("<Button-1>", lambda event: self.animation5(self.var + 4))
            self.image6.bind("<Button-1>", lambda event: self.animation5(self.var + 5))
            self.image7.bind("<Button-1>", lambda event: self.animation5(self.var + 6))
            ##_______________________________End Slider Images____________________

            # Scanfolder
            self.scanfile(self.adress.get(), self.IMAGE)
            # Menubar
            self.IMAGE_NAME(self.var)
            self.collaps_expand_button = tk.Label(self.menubar)
            self.collaps_expand_button.pack(anchor='ne', padx=1, pady=10, side='right')
            self.collaps_expand_button.bind("<Button-1>", self.menubar_expand)
            self.menubar_expand()

            self.mainloop()

        # _______________________________________________________________________________________________Functions Starts

        def menubar_expand(self, event=None):

            if self.menubar_var != 400:
                self.menubar.place(width=self.menubar_var)
                self.menubar_var += 20
                self.menubar.after(10, self.menubar_expand)

            else:
                self.createmenubar()
                try:
                    self.collaps_expand_button.configure(text="<")
                    self.collaps_expand_button.bind("<Button-1>", self.menubar_collaps)
                except:
                    pass

        def menubar_collaps(self, event=None):

            try:

                self.searchmenu.destroy()
                self.selectfolder.destroy()
                self.combobox.destroy()
                self.button.destroy()
                self.keys.destroy()
                self.Image_name.destroy()
                self.MainFrame.destroy()
            except:
                pass
            if self.menubar_var != 20:
                self.menubar.place(width=self.menubar_var)
                self.menubar_var -= 20
                self.menubar.after(30, self.menubar_collaps)
            if self.menubar_var == 20:
                try:
                    self.collaps_expand_button.configure(text=">")
                    self.collaps_expand_button.bind("<Button-1>", self.menubar_expand)
                except:
                    pass

        def createmenubar(self):

            self.IamgeDetail_Width = 0
            self.p = tk.StringVar()

            def action_():

                self.height = 30
                copy_bg = 'cyan'
                move_bg = 'lightgreen'
                delete_bg = 'orange'

                labelfont = ('courier', 10, 'bold')
                entryfont = ('courier', 10, 'italic')
                buttonfont = ('impact', 10, 'bold')

                def setpath(event=None):
                    a = filedialog.askdirectory()
                    self.p.set(a)

                def refresh():
                    self.filename.pop(self.var)
                    self.pilimagefile.pop(self.var)
                    self.filepathlist.pop(self.var)
                    self.resizeimage.pop(self.var)
                    self.ImageNewShow()
                    self.update()

                def not_normal():
                    def normal():
                        self.statusbar.configure(text="Take A Action", bg='white')
                        self.selectpath_entry.configure(bg="white")
                        self.selectpath_entry.configure(state=tk.DISABLED, bg="white")

                    self.statusbar.configure(text="Please Select Location", bg='red')
                    self.selectpath_entry.configure(state="normal", bg="red")
                    self.after(700, normal)

                def copy_file(event=None):
                    if len(self.selectpath_entry.get()) > 0:
                        filename = self.filepathlist[self.var]
                        destination = os.path.join(self.p.get(), self.filename[self.var])
                        shutil.copyfile(filename, destination)
                        self.statusbar.configure(text="Succefully Copy")
                        self.sumbit.configure(bg="blue")
                        self.after(700, lambda event=None: self.sumbit.configure(bg="white"))

                    else:
                        self.sumbit.configure(bg="red")
                        self.after(700, lambda event=None: self.sumbit.configure(bg="white"))
                        not_normal()

                    # Notifier.notify("Successfully Copy")

                def move_file(event=None):
                    if len(self.selectpath_entry.get()) > 0:
                        filename = self.filepathlist[self.var]
                        destination = os.path.join(self.p.get(), self.filename[self.var])
                        shutil.move(filename, destination)
                        refresh()
                        self.statusbar.configure(text="Succesfully Move")
                        self.sumbit1.configure(bg="blue")
                        self.after(700, lambda event=None: self.sumbit.configure(bg="white"))
                    else:
                        not_normal()
                        self.sumbit2.configure(bg="red")
                        self.selectpath_entry.configure(bg='red')
                        self.after(700, lambda event=None: self.sumbit2.configure(bg="white"))

                    # Notifier.notify("Successfully Move")

                def delete_file(event=None):
                    filename = self.filepathlist[self.var]
                    os.remove(filename)
                    refresh()
                    self.sumbit3.configure(bg="blue")
                    self.after(700, lambda event=None: self.sumbit3.configure(bg="white"))

                    # Notifier.notify("Successfully Delete")

                def down():

                    if self.height != 300:
                        self.MainFrame.place(height=self.height)
                        self.height += 15
                        self.update()
                        self.MainFrame.after(1, down)

                def up():

                    if self.height > 90:
                        self.MainFrame.place(height=self.height)
                        self.height -= 90
                        self.MainFrame.after(1, up)
                        self.update()

                def copy_b(event=None):
                    try:
                        self.actionarea.destroy()
                    except:
                        pass

                    bg = copy_bg
                    if self.height == 300:
                        up()
                    elif self.height == 30:
                        down()
                    else:
                        pass
                    self.actionarea = tk.Label(self.MainFrame, bg=bg)
                    self.actionarea.place(y=40, relwidth=1, relheight=1)
                    self.MainFrame.place(relwidth=1)

                    path = tk.Label(self.actionarea, text='File Location', bg=bg, font=labelfont)
                    pathentry = tk.Entry(self.actionarea, bg='lightyellow', fg='black', textvariable=self.file_adress,
                                         font=entryfont)
                    selectpath = tk.Label(self.actionarea, text='Select Location (Copy)', bg=bg, font=labelfont)
                    self.selectpath_entry = tk.Entry(self.actionarea, bg='lightyellow', fg='black', font=entryfont,
                                                     textvariable=self.p, state=tk.DISABLED)
                    self.statusbar = tk.Label(self.actionarea, text="Take A Action")

                    self.file_adress.set(self.filepathlist[self.var])

                    copy_move_delete = tk.Label(self.actionarea)
                    self.sumbit = tk.Button(copy_move_delete, text='Copy', font=buttonfont, command=copy_file)
                    self.sumbit2 = tk.Button(copy_move_delete, text='Move', font=buttonfont, command=move_file)
                    self.sumbit3 = tk.Button(copy_move_delete, text='Delete', font=buttonfont, command=delete_file)

                    copy_move_delete.pack(fill=tk.X)
                    self.sumbit.grid(row=0, column=0, padx=10)
                    self.sumbit2.grid(row=0, column=1, padx=10)
                    self.sumbit3.grid(row=0, column=2, padx=10)
                    self.statusbar.pack(fill=tk.X)

                    path.pack(fill=tk.X)
                    pathentry.pack(fill=tk.X, pady=10)
                    selectpath.pack(fill=tk.X)
                    self.selectpath_entry.pack(fill=tk.X, pady=10)
                    self.selectpath_entry.bind("<Button-1>", setpath)

                    self.bind("<KeyPress-1>", copy_file)
                    self.bind("<KeyPress-2>", move_file)
                    self.bind("<KeyPress-3>", delete_file)

                self.MainFrame = tk.LabelFrame(self.menubar, text='Action Keys', bg='black', fg='gold',
                                               font=('menio', 30, 'bold'))
                self.MainFrame.place(y=250, x=0, relwidth=1)
                copy = tk.Label(self.MainFrame, text='copy', bg=copy_bg, width=12)
                copy.bind('<Button-1>', copy_b)
                copy.grid(row=0, column=1)
                copy_b()

            def listbox_botton(event=None):
                self.search_text.delete(0, tk.END)
                self.animation5(self.listbox.curselection()[0])
                self.search_text.insert(0, self.listbox.get(self.listbox.curselection()[0]))
                self.keys.destroy()

            def listboxcreator(event):
                self.listbox.delete(0, tk.END)
                for i in self.filename:
                    if i.find(self.search_text.get()) != -1:
                        self.listbox.insert(tk.END, i)

            def searchtext_focus(event):

                try:
                    self.search_number.destroy()
                except:
                    pass
                try:
                    self.listbox.destroy()
                except:
                    pass
                try:
                    self.MainFrame.destroy()
                except:
                    pass

                scrollbar = tk.Scrollbar(self.searchmenu, orient='vertical')
                scrollbar1 = tk.Scrollbar(self.searchmenu, orient='horizontal')
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                scrollbar1.pack(side=tk.BOTTOM, fill=tk.X)

                self.search_text.delete(0, tk.END)
                self.searchmenu.place(relheight=1, relwidth=1)
                self.searchmenu.configure(bg='black', relief='sunken')
                self.listbox = tk.Listbox(self.searchmenu, bd=10, bg='gold', highlightthickness=3, relief='solid',
                                          yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1.set)
                [self.listbox.insert(tk.END, i) for i in self.filename]
                self.listbox.bind("<ButtonRelease>", listbox_botton)
                self.listbox.bind("<KeyRelease>", listbox_botton)
                scrollbar.config(command=self.listbox.yview)
                scrollbar1.config(command=self.listbox.xview)
                self.listbox.place(relwidth=1, relheight=1)

            def searchtext_out(event=None):

                try:
                    self.searchmenu.destroy()

                except:
                    pass
                try:
                    self.MainFrame.destroy()
                except:
                    pass
                self.search_number_var.set(self.number)

                self.searchmenu = tk.LabelFrame(self.menubar, height=300, bg='black', fg='gold', text='Find ',
                                                font=('menio', 30, 'bold'))
                self.searchmenu.place(x=0, y=100, relwidth=1, height=200)

                self.search_text = ttk.Entry(self.searchmenu, width=25)
                self.search_text.place(relwidth=1)
                self.search_text.after(100, lambda: self.search_text.insert(tk.END, 'S'))
                self.search_text.after(200, lambda: self.search_text.insert(tk.END, 'e'))
                self.search_text.after(300, lambda: self.search_text.insert(tk.END, 'a'))
                self.search_text.after(400, lambda: self.search_text.insert(tk.END, 'r'))
                self.search_text.after(500, lambda: self.search_text.insert(tk.END, 'c'))
                self.search_text.after(600, lambda: self.search_text.insert(tk.END, 'h'))
                self.search_text.after(601, lambda: self.search_text.delete(0, tk.END))
                self.search_text.after(610, lambda: self.search_text.insert(tk.END, 'Search'))

                self.search_number = ttk.Entry(self.searchmenu, width=25,
                                               state='normal')
                self.search_number.place(relwidth=1, y=40)
                self.search_number.after(100, lambda: self.search_number.insert(tk.END, 'S'))
                self.search_number.after(200, lambda: self.search_number.insert(tk.END, 'e'))
                self.search_number.after(300, lambda: self.search_number.insert(tk.END, 'a'))
                self.search_number.after(400, lambda: self.search_number.insert(tk.END, 'r'))
                self.search_number.after(500, lambda: self.search_number.insert(tk.END, 'c'))
                self.search_number.after(600, lambda: self.search_number.insert(tk.END, 'h'))
                self.search_number.after(700, lambda: self.search_number.configure(textvariable=self.search_number_var))

                self.search_number.bind("<Button-1>", self.search_focus)
                self.search_number.bind("<FocusOut>", self.search_focus_out)
                self.search_number.bind("<KeyRelease>", self.search_key_press)
                self.search_number.bind("<KeyPress>", self.search_key_pr)

                self.search_text.bind("<FocusIn>", searchtext_focus)
                self.menubar.bind("<Button-1>", searchtext_out)
                self.search_text.bind("<KeyRelease>", listboxcreator)
                self.search_text.bind("<ButtonRelease>", listboxcreator)

                action_()

            self.selectfolder = ttk.Entry(self.menubar, textvariable=self.adress)

            self.combobox = ttk.Combobox(self.menubar, value=self.IMAGE, state='readonly')
            self.combobox.current(0)
            self.button = ttk.Button(self.menubar, text='Select', command=self.SUMBIT,
                                     width=15)
            self.selectfolder.bind("<ButtonRelease>", self.choosefolder)

            self.keys = tk.LabelFrame(self.menubar, height=50, bg='red')
            self.keys.pack(fill=tk.X, side='bottom')
            backkey = ttk.Button(self.keys, text="Previous", command=self.Back).pack(anchor='ne', side='left')
            nextkey = ttk.Button(self.keys, text="Next", command=self.Next).pack(anchor='nw', side='right')
            show = ttk.Button(self.keys, text="Show", command=self.show).pack(side='top')

            # Previous
            self.bind("<Left>", self.Back)
            self.bind("<Right>", self.Next)

            self.Image_name = tk.Label(self.menubar, text='None', wraplength=300)
            self.Image_name.pack(side='bottom')

            # self.search_text.bind("<FocusIn>",self.search_focusin)
            # self.search_text.bind("<FocusOut>", self.search_focus_outs)
            # CREATING A CONTROLS

            self.selectfolder.pack(fill=tk.X, padx=10, pady=10, anchor='nw', side='top')
            self.button.pack(anchor='ne', side='right', pady=10)
            self.combobox.pack(pady=10, padx=10, fill=tk.X, side='top', anchor='nw')
            searchtext_out()
            self.ImageName()

        def ImageName(self):
            if self.IamgeDetail_Width != 50:
                self.IamgeDetail_Width += 2
                self.Image_name.configure(width=self.IamgeDetail_Width)
                self.Image_name.after(10, self.ImageName)
            else:
                self.IamgeDetail_Width = 0

        def SUMBIT(self):

            if self.combobox.get() == 'ALL':
                self.scanfile(self.selectfolder.get(), self.IMAGE)
            else:
                self.scanfile(self.selectfolder.get(), self.combobox.get())

        def show(self, event=None):

            image = Image.open(self.filepathlist[self.var])
            image.show()

        def search_focus(self, event):
            if self.search_number_var.get() == self.number:
                self.search_number.configure(state='normal')
                self.search_number_var.set('')
            elif self.search_number_var.get() == 'Please enter only numbers !' or self.search_number_var.get() == "So long!":
                self.search_number_var.set("Wait....")

        def search_focus_out(self, event):
            self.search_number.configure(state='disable')
            if self.search_number_var.get() == '':
                self.search_number_var.set(self.number)

        def search_key_press(self, event):
            try:
                int(self.search_number_var.get())
            except:
                if len(self.search_number_var.get()) != 0:
                    self.search_number.configure(state='disable')
                    self.search_number_var.set("Please enter only numbers !")
                    self.search_number.after(1500, lambda: self.search_number_var.set(self.number))


            else:
                if int(self.search_number_var.get()) > int(self.totalimages):
                    self.search_number.configure(state='disable')
                    self.search_number_var.set("So long!")
                    self.search_number.after(1500, lambda: self.search_number_var.set(self.number))
                else:
                    self.animation5(int(self.search_number_var.get()))

        def search_key_pr(self, event):
            if self.search_number_var.get() == self.number:
                self.search_number.configure(state='normal')
                self.search_number_var.set('')

        def choosefolder(self, event):
            file1 = "C:\\Users"
            file1 = filedialog.askdirectory()

            self.adress.set(file1)

        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&__________________________

        def scanfile(self, adress, *args):
            if self.active == 0:
                self.active = 1
                IMAGE = args

                def a1():
                    Loading.configure(text='Loading', fg='white')
                    Loading.after(500, a2)

                def a2():
                    Loading.configure(text='Loading.', fg='red')
                    Loading.after(500, a3)

                def a3():
                    Loading.configure(text='Loading..', fg='blue')
                    Loading.after(500, a4)

                def a4():
                    Loading.configure(text='Loading...', fg='green')
                    Loading.after(500, a1)

                Loading = tk.Label(self.frame3, text='Loading', font=('didot', 30, 'bold'), bg='black', fg='white')

                Loading.pack(expand=True, fill='both', pady=10)
                a1()

                try:
                    self.Scalebar.set(0)
                except:
                    pass
                try:
                    self.Scalebar.destroy()
                except:
                    pass
                self.var = 0

                vars = 0
                self.pilimagefile = []
                self.resizeimage = []
                self.filepathlist = []
                self.filename = []

                # _____________________________________________________Gathering All Image files

                for i, j, l in os.walk(adress):
                    for filename in l:

                        for ext in IMAGE:
                            if filename.endswith(ext):
                                path = os.path.join(i, filename)
                                self.filepathlist.append(path)
                                self.filename.append(filename)
                                self.update()

                Loading.destroy()
                lent = len(self.filename)
                self.totalimages = lent
                try:
                    self.Scalebar['to'] = self.totalimages
                except:
                    pass

                self.number = f'Search 0 - {self.totalimages}'
                try:
                    self.search_number_var.set(self.number)
                except:
                    pass
                Loading = tk.Label(self.frame3, text=f' {lent} ', font=('didot', 30, 'bold'), bg='black', fg='white')

                Loading.pack(expand=True, fill='both', pady=10)

                for i in self.filepathlist:

                    try:
                        l1 = Image.open(i)
                        width, height = l1.size
                        try:
                            l2 = l1.resize((100, 70))
                            self.resizeimage.append(ImageTk.PhotoImage(l2))

                        except:
                            self.resizeimage.append(ImageTk.PhotoImage(l1))

                        # MAIN IMAGE SIZE CONVERSIONS_________________________________
                        if width > height:

                            if width > self.landscape_setwidth or height > self.landscape_setheight:
                                l3 = l1.resize((self.landscape_setheight, self.landscape_setheight))
                                self.pilimagefile.append(ImageTk.PhotoImage(l3))

                            else:
                                self.pilimagefile.append(ImageTk.PhotoImage(l1))
                        else:

                            if width > self.patrait_setwidth or height > self.patrait_setheight:
                                l3 = l1.resize((self.patrait_setwidth, self.patrait_setheight))
                                self.pilimagefile.append(ImageTk.PhotoImage(l3))

                            else:
                                self.pilimagefile.append(ImageTk.PhotoImage(l1))

                        vars += 1
                        Loading.configure(text=f'{lent} / {vars}')
                        self.ImageNewShow()
                        self.update()


                    except:

                        var = len(self.pilimagefile)
                        try:
                            self.filename.pop(var)
                        except:
                            pass
                        try:
                            self.filepathlist.pop(var)
                        except:
                            pass
                        try:
                            self.pilimagefile.pop(var)
                        except:
                            pass
                        try:
                            self.resizeimage.pop(var)
                        except:
                            pass

                self.animation()

                # ScaleBar

                self.Scalebar = tk.Scale(self, from_=0, to=self.totalimages,
                                         command=lambda event: self.animation5(int(self.Scalebar.get())),
                                         orient='horizontal',
                                         bg='black', fg='white', activebackground='red', troughcolor='yellow')

                # self.Scalebar.pack(side='bottom', fill=tk.X, pady=10)
                self.Scalebar.place(x=370, y=720, width=self.winfo_width() - 400)
                Loading.destroy()
                self.active = 0
            else:

                messagebox.showwarning("Already Running",
                                       "Alredy Progress Are running please wait until the process is compleate")

        def ImageNewShow(self, event=None):

            try:
                self.mainphoto.configure(image=self.pilimagefile[self.var])
                self.Scalebar.set(self.var)


            except:
                self.mainphoto.configure(image=self.notfoumdimage)

            try:
                self.image1.configure(image=self.resizeimage[self.var])
                self.name1.configure(text=1 + self.var, fg='gold')
                self.file1.configure(text=self.filename[self.var][0:25])
            except:
                self.image1.configure(image=self.notfoumdimage)
                self.name1.configure(text="Not Available", fg='red')
                self.file1.configure(text='')

            try:
                self.image2.configure(image=self.resizeimage[1 + self.var])
                self.name2.configure(text=2 + self.var, fg='gold')
                self.file2.configure(text=self.filename[1 + self.var][0:25])
            except:
                self.image2.configure(image=self.notfoumdimage)
                self.name2.configure(text="Not Available", fg='red')
                self.file2.configure(text='')

            try:
                self.image3.configure(image=self.resizeimage[2 + self.var])
                self.name3.configure(text=3 + self.var, fg='gold')
                self.file3.configure(text=self.filename[2 + self.var][0:25])
            except:
                self.image3.configure(image=self.notfoumdimage)
                self.name3.configure(text="Not Available", fg='red')
                self.file3.configure(text='')
            try:
                self.image4.configure(image=self.resizeimage[3 + self.var])
                self.name4.configure(text=4 + self.var, fg='gold')
                self.file4.configure(text=self.filename[3 + self.var][0:25])

            except:
                self.image4.configure(image=self.notfoumdimage)
                self.name4.configure(text="Not Available", fg='red')
                self.file4.configure(text='')
            try:
                self.image5.configure(image=self.resizeimage[4 + self.var])
                self.name5.configure(text=5 + self.var, fg='gold')
                self.file5.configure(text=self.filename[4 + self.var][0:25])
            except:
                self.image5.configure(image=self.notfoumdimage)
                self.name5.configure(text="Not Available", fg='red')
                self.file5.configure(text='')
            try:
                self.image6.configure(image=self.resizeimage[5 + self.var])
                self.name6.configure(text=6 + self.var, fg='gold')
                self.file6.configure(text=self.filename[5 + self.var][0:25])

            except:
                self.image6.configure(image=self.notfoumdimage)
                self.name6.configure(text="Not Available", fg='red')
                self.file6.configure(text='')
            try:
                self.image7.configure(image=self.resizeimage[6 + self.var])
                self.name7.configure(text=7 + self.var, fg='gold')
                self.file7.configure(text=self.filename[6 + self.var][0:25])

            except:
                self.image7.configure(image=self.notfoumdimage)
                self.name7.configure(text="Not Available", fg='red')
                self.file7.configure(text='')

        def animation(self):
            # slider go to next
            if self.animationvariable != 170:

                if self.animationvariable < 100:
                    self.image1.place(x=70 - self.animationvariable + 10, y=1, width=130, height=100)


                else:
                    self.image1.place(x=0 - self.animationvariable + 10, y=0, width=130, height=100)

                self.image2.place(x=270 - self.animationvariable)
                self.image3.place(x=470 - self.animationvariable)
                self.image4.place(x=670 - self.animationvariable)
                self.image5.place(x=870 - self.animationvariable)
                self.image6.place(x=1070 - self.animationvariable)
                self.image7.place(x=1270 - self.animationvariable)

                self.name1.place(x=70 - self.animationvariable)
                self.name2.place(x=270 - self.animationvariable)
                self.name3.place(x=470 - self.animationvariable)
                self.name4.place(x=670 - self.animationvariable)
                self.name5.place(x=870 - self.animationvariable)
                self.name6.place(x=1070 - self.animationvariable)
                self.name7.place(x=1270 - self.animationvariable)

                self.file1.place(x=40 - self.animationvariable, y=1)
                self.file2.place(x=240 - self.animationvariable, y=1)
                self.file3.place(x=440 - self.animationvariable, y=1)
                self.file4.place(x=640 - self.animationvariable, y=1)
                self.file5.place(x=840 - self.animationvariable, y=1)
                self.file6.place(x=1040 - self.animationvariable, y=1)
                self.file7.place(x=1240 - self.animationvariable, y=1)

                self.animationvariable += 10

                self.frame2.after(10, lambda: self.animation())



            else:

                self.image1.place(x=70)
                self.image2.place(x=270)
                self.image3.place(x=470)
                self.image4.place(x=670)
                self.image5.place(x=870)
                self.image6.place(x=1070)
                self.image7.place(x=1270)

                self.name1.place(x=70)
                self.name2.place(x=270)
                self.name3.place(x=470)
                self.name4.place(x=670)
                self.name5.place(x=870)
                self.name6.place(x=1070)
                self.name7.place(x=1270)

                self.file1.place(x=40, y=20)
                self.file2.place(x=240, y=20)
                self.file3.place(x=440, y=20)
                self.file4.place(x=640, y=20)
                self.file5.place(x=840, y=20)
                self.file6.place(x=1040, y=20)
                self.file7.place(x=1240, y=20)

                self.animationvariable = 0
                self.ImageNewShow()

        def animation1(self):
            # slider goto back animation
            if self.animationvariable != 170:
                self.image1.place(x=70 + self.animationvariable)
                self.image2.place(x=270 + self.animationvariable)
                self.image3.place(x=470 + self.animationvariable)
                self.image4.place(x=670 + self.animationvariable)
                self.image5.place(x=870 + self.animationvariable)
                self.image6.place(x=1070 + self.animationvariable)
                self.image7.place(x=1270 + self.animationvariable)

                self.name1.place(x=70 + self.animationvariable)
                self.name2.place(x=270 + self.animationvariable)
                self.name3.place(x=470 + self.animationvariable)
                self.name4.place(x=670 + self.animationvariable)
                self.name5.place(x=870 + self.animationvariable)
                self.name6.place(x=1070 + self.animationvariable)
                self.name7.place(x=1270 + self.animationvariable)

                self.file1.place(x=40 + self.animationvariable, y=1)
                self.file2.place(x=250 + self.animationvariable, y=1)
                self.file3.place(x=450 + self.animationvariable, y=1)
                self.file4.place(x=650 + self.animationvariable, y=1)
                self.file5.place(x=850 + self.animationvariable, y=1)
                self.file6.place(x=1050 + self.animationvariable, y=1)
                self.file7.place(x=1250 + self.animationvariable, y=1)
                self.animationvariable += 10

                self.frame2.after(10, lambda: self.animation1())


            else:
                self.image1.place(x=70)
                self.image2.place(x=270)
                self.image3.place(x=470)
                self.image4.place(x=670)
                self.image5.place(x=870)
                self.image6.place(x=1070)
                self.image7.place(x=1270)
                self.name1.place(x=70)
                self.name2.place(x=270)
                self.name3.place(x=470)
                self.name4.place(x=670)
                self.name5.place(x=870)
                self.name6.place(x=1070)
                self.name7.place(x=1270)
                self.file1.place(x=40, y=20)
                self.file2.place(x=240, y=20)
                self.file3.place(x=440, y=20)
                self.file4.place(x=640, y=20)
                self.file5.place(x=840, y=20)
                self.file6.place(x=1040, y=20)
                self.file7.place(x=1240, y=20)

                self.animationvariable = 0
                self.ImageNewShow()

        def animation3(self):
            # main image goto next animation
            if self.animationvariable1 != 400:
                self.mainphoto.place(width=self.animationvariable1)
                # self.mainphoto.configure(height=self.animationvariable1)
                self.animationvariable1 += 10
                self.mainphoto.after(1, self.animation3)
            else:
                self.mainphoto.place(relwidth=1, relheight=1)
                self.animationvariable1 = 0

        def animation4(self):
            # main image goto back animation
            if self.animationvariable3 != 100:
                self.mainphoto.place(width=self.animationvariable3)
                self.animationvariable3 = self.animationvariable3 - 10
                self.mainphoto.after(1, self.animation4)

            else:
                self.mainphoto.place(relwidth=1, relheight=1)
                self.animationvariable3 = 400

        def animation5(self, number):
            # Slider go to direct  number animation

            if number <= self.totalimages:
                if self.var < number:
                    self.animation()
                    self.animation3()
                    self.var = number
                    try:
                        self.Scalebar.set(self.var)
                    except:
                        pass
                    self.IMAGE_NAME(self.var)
                    self.file_adress.set(self.filepathlist[self.var])



                elif self.var > number:
                    self.var = number
                    self.animation1()
                    self.animation4()
                    self.var = number
                    self.Scalebar.set(self.var)
                    self.IMAGE_NAME(self.var)
                    self.file_adress.set(self.filepathlist[self.var])

        def IMAGE_NAME(self, var):
            try:
                try:
                    self.Image_name.configure(text=self.filename[self.var])
                except:
                    pass
                # self.imagedeatil.configure(text=f"Image Number {self.var}")
            except:
                try:
                    self.Image_name.configure(text="Not Found")
                except:
                    pass
                # self.imagedeatil.configure(text=f"Not Available")

        def Next(self, event=None):
            if self.var != self.totalimages:
                self.ImageName()
                self.animation()
                self.animation3()
                self.var += 1
                try:
                    self.file_adress.set(self.filepathlist[self.var])

                except:
                    tk.messagebox.showerror("End Images", "Images are end no more images")

                try:
                    self.file_adress.set(self.filepathlist[self.var])
                except:
                    self.file_adress.set("Not Found")
                self.IMAGE_NAME(self.var)
                self.update()

        def Back(self, event=None):

            if self.var != 0:
                self.ImageName()
                self.var = self.var - 1
                try:
                    self.file_adress.set(self.filepathlist[self.var])

                except:
                    self.file_adress.set("Not Found")

                self.animation1()
                self.animation4()
                try:
                    self.Scalebar.set(self.var)
                except:
                    pass
                self.Image_name.configure(text=self.filename[self.var])
                self.IMAGE_NAME(self.var)
                self.update()
                # Shiorcuts


    k = Images()








except:
    print("Error")