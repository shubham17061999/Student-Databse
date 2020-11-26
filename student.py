#frontend

from tkinter import*
import tkinter.messagebox
import stdDatabase_BackEnd

class Student:

	def __init__(self,root):
		self.root=root
		self.root.title("Student Database Management System")
		self.root.geometry("1350x7500+0+0")
		self.root.config(bg="dark grey")

		StdID = StringVar()
		Firstname = StringVar()
		Surname = StringVar()
		DoB = StringVar()
		Age = StringVar()
		Gender = StringVar()
		Address = StringVar()
		Mobile = StringVar()

#************************************************functions
		def iExit():# add to exit button widget besides bd      command=iExit
			iExit = tkinter.messagebox.askyesno("Student's Database Systems","Hope you are satistfied")
			if iExit > 0:
				root.destroy()
				return
		def clearData():#add to clear button widget besides bd    command=clearData
			self.txtStdID.delete(0,END)
			self.txtfna.delete(0,END)
			self.txtSna.delete(0,END)
			self.txtDoB.delete(0,END)
			self.txtAge.delete(0,END)
			self.txtGender.delete(0,END)
			self.txtAdr.delete(0,END)
			self.txtMoblie.delete(0,END)


		def addData():#add to the add button widget besides bd     command=addData
			if(len(StdID.get())!=0):
				stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),\
				                              Address.get(), Mobile.get())
				studentlist.delete(0,END)
				studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), \
				                   Address.get(), Mobile.get()))

		def DisplayData():#add to the display data button widget besides bd     command=DisplayData
			studentlist.delete(0,END)
			for row in stdDatabase_BackEnd.viewData():
				studentlist.insert(END,row,str(""))

		def StudentRec(event):#in listbox and scrollbar we have called it
			global sd
			searchStd = studentlist.curselection()[0]
			sd = studentlist.get(searchStd)

			self.txtStdID.delete(0,END)
			self.txtStdID.insert(END,sd[1])
			self.txtfna.delete(0,END)
			self.txtfna.insert(END,sd[2])
			self.txtSna.delete(0,END)
			self.txtSna.insert(END,sd[3])
			self.txtDoB.delete(0,END)
			self.txtDoB.insert(END,sd[4])
			self.txtAge.delete(0,END)
			self.txtAge.insert(END,sd[5])
			self.txtGender.delete(0,END)
			self.txtGender.insert(END,sd[6])
			self.txtAdr.delete(0,END)
			self.txtAdr.insert(END,sd[7])
			self.txtMoblie.delete(0,END)
			self.txtMoblie.insert(END,sd[8])

		def DeleteData():#add in delete data button beside bd     command=DeleteData
			 if(len(StdID.get())!=0):
			 	stdDatabase_BackEnd.deleteRec(sd[0])
			 	studentlist.delete(0,END)

	 			clearData()
	 			DisplayData() 

		def searchDatabase():
			studentlist.delete(0,END)
			for row in stdDatabase_BackEnd.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),Address.get(), Mobile.get()):
				studentlist.insert(END,row,str(""))

		def update():
			
			if(len(StdID.get())!=0):
				
				stdDatabase_BackEnd.deleteRec(sd[0])
				

			if(len(StdID.get())!=0):
				stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),Address.get(), Mobile.get())
				studentlist.delete(0,END)
				studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),Address.get(), Mobile.get()))

				
  #frames********************************************
		MainFrame = Frame(self.root, bg="dark grey")
		MainFrame.grid()

		TitFrame = Frame(MainFrame, bd=2, padx=70, pady=8 ,bg="black", relief=RIDGE)
		TitFrame.pack(side=TOP)

		self.lblTit=Label(TitFrame , font=('Calibri',40,'bold'),text="Student Database Management Systems",bg="ghost white")
		self.lblTit.grid()

		ButtonFrame = Frame(MainFrame, width=1350, height=70, padx=20,pady=10 ,bg="Ghost White", relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		DataFrame = Frame(MainFrame, width=1300, height=400, padx=20,pady=20 ,bg="dark grey", relief=RIDGE)
		DataFrame.pack(side=BOTTOM)

		DataFrameLEFT = LabelFrame(DataFrame,bd=1, width=1000, height=400, padx=18,bg="Ghost White", relief=RIDGE, font=('Calibri',25,'bold'),text="Student Information\n")
		DataFrameLEFT.pack(side=LEFT)

		DataFrameRIGHT = LabelFrame(DataFrame,bd=1, width=550, height=300, padx=31,pady=3,bg="Ghost White",relief=RIDGE,font=('Calibri',25,'bold'),text="Student Details\n")
		DataFrameRIGHT.pack(side=RIGHT)

		#labels and entry widget*******************************************************
		
		self.lblStdID=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Student ID:",padx=2, pady=2,bg="ghost white")
		self.lblStdID.grid(row=0,column=0, sticky=W)
		self.txtStdID=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=StdID, width=39)
		self.txtStdID.grid(row=0,column=1)

		self.lblfna=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="FirstName:",padx=2, pady=2,bg="ghost white")
		self.lblfna.grid(row=1,column=0, sticky=W)
		self.txtfna=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Firstname , width=39)
		self.txtfna.grid(row=1,column=1)

		self.lblSna=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Surname:",padx=2, pady=2,bg="ghost white")
		self.lblSna.grid(row=2,column=0, sticky=W)
		self.txtSna=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Surname, width=39)
		self.txtSna.grid(row=2,column=1)

		self.lbldob=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Date of Birth:",padx=2, pady=2,bg="ghost white")
		self.lbldob.grid(row=3,column=0, sticky=W)
		self.txtDoB=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=DoB, width=39)
		self.txtDoB.grid(row=3,column=1)

		self.lblage=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Age:",padx=2, pady=2,bg="ghost white")
		self.lblage.grid(row=4,column=0, sticky=W)
		self.txtAge=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Age, width=39)
		self.txtAge.grid(row=4,column=1)

		self.lblgender=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Gender:",padx=2, pady=2,bg="ghost white")
		self.lblgender.grid(row=5,column=0, sticky=W)
		self.txtGender=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Gender, width=39)
		self.txtGender.grid(row=5,column=1)

		self.lbladr=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Address:",padx=2, pady=2,bg="ghost white")
		self.lbladr.grid(row=6,column=0, sticky=W)
		self.txtAdr=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Address, width=39)
		self.txtAdr.grid(row=6,column=1)

		self.lblMobile=Label(DataFrameLEFT , font=('Calibri',20,'bold'),text="Mobile:",padx=2, pady=2,bg="ghost white")
		self.lblMobile.grid(row=7,column=0, sticky=W)
		self.txtMoblie=Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Mobile, width=39)
		self.txtMoblie.grid(row=7,column=1)

#Listbox************************************************************************************************************
		scrollbar= Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0,column=1, sticky='ns') 

		studentlist = Listbox(DataFrameRIGHT, width=41, height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
		studentlist.bind('<<listboxSelect>>',StudentRec)
		studentlist.grid(row=0,column=0, padx=8)
  		

#Buttons**********************************************************************************************************************
		self.btnAddData= Button(ButtonFrame,text="Add New",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=addData)
		self.btnAddData.grid(row=0,column=0)

		self.btnDisplayData= Button(ButtonFrame,text="Display",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
		self.btnDisplayData.grid(row=0,column=1)

		self.btnClearData= Button(ButtonFrame,text="Clear",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=clearData)
		self.btnClearData.grid(row=0,column=2)

		self.btnDeleteData= Button(ButtonFrame,text="Delete",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
		self.btnDeleteData.grid(row=0,column=3)

		self.btnSearchData= Button(ButtonFrame,text="Search",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
		self.btnSearchData.grid(row=0,column=4)

		self.btnUpdateData= Button(ButtonFrame,text="Update",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=update)
		self.btnUpdateData.grid(row=0,column=5)

		self.btnExit= Button(ButtonFrame,text="Exit",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=iExit)
		self.btnExit.grid(row=0,column=6)

		






if __name__=='__main__':
	root =Tk()
	application = Student(root)
	root.mainloop()

   