import customtkinter
import pandas as pd
import pickle
from tkinter import messagebox

# Load a saved pickle model and evaluate it
loaded_pickle_model = pickle.load(open("random_forest_model_1.pkl", "rb"))

class MyScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="white") 
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=1)

        # Asking for the name of the user
        self.label1 = customtkinter.CTkLabel(self, text="Name:", text_color="black")
        self.label1.grid(row=1, column=1, pady=10)    
        self.name = customtkinter.CTkEntry(self)
        self.name.grid(row=1, column=2, pady=10)
        
    
        # Asking for the age of the user
        self.label2 = customtkinter.CTkLabel(self, text="Age(in yrs):", text_color="black")
        self.label2.grid(row=2, column=1, pady=10)    
        self.age = customtkinter.CTkEntry(self)
        self.age.grid(row=2, column=2, pady=10)
        
        # Asking for the sex of the user
        def gender_callback(choice):
            self.gender.set(choice)
        self.label3 = customtkinter.CTkLabel(self, text="Gender:", text_color="black")
        self.label3.grid(row=3, column=1, pady=10)    
        self.gender = customtkinter.CTkOptionMenu(master=self, values=["Male", "Female"],
                                         command=gender_callback)
        self.gender.grid(row=3, column=2, pady=10)
        
        
        # Asking for the chestPainType of the user
        def cp_callback(choice):
            self.cp.set(choice)
        self.label4 = customtkinter.CTkLabel(self, text="cp : \nChest pain type", text_color="black")
        self.label4.grid(row=4, column=1, pady=10)    
        self.cp = customtkinter.CTkOptionMenu(master=self, values=["typical angina", "atypical angina", "non-anginal pain", "asymptomatic"],
                                         command=cp_callback)
        self.cp.grid(row=4, column=2, pady=10)
        
        # ASking for the Resting Blood Pressure
        self.label5 = customtkinter.CTkLabel(self, text="trestbps : \nResting blood pressure (mm Hg)")
        self.label5.grid(row=5, column=1, pady=10)
        self.trestbps = customtkinter.CTkEntry(self)
        self.trestbps.grid(row=5, column=2, pady=10)

        # ASking for the Serum Cholestrol
        self.label6 = customtkinter.CTkLabel(self, text="chol : \nSerum cholesterol (mg/dl)")
        self.label6.grid(row=6, column=1, pady=10)
        self.chol = customtkinter.CTkEntry(self)
        self.chol.grid(row=6, column=2, pady=10)

        # Asking for the Fasting Blood Sugar of the user
        def fbs_callback(choice):
            self.fbs.set(choice)
        self.label7 = customtkinter.CTkLabel(self, text="fbs : \nFasting blood sugar > 120 mg/dl", text_color="black")
        self.label7.grid(row=7, column=1, pady=10)    
        self.fbs = customtkinter.CTkOptionMenu(master=self, values=["true", "false"],
                                         command=fbs_callback)
        self.fbs.grid(row=7, column=2, pady=10)

        # Asking for the Resting electrocardiographic results of the user
        def restecg_callback(choice):
            self.restecg.set(choice)
        self.label8 = customtkinter.CTkLabel(self, text="restecg : \nResting electrocardiographic results", text_color="black")
        self.label8.grid(row=8, column=1, pady=10)    
        self.restecg = customtkinter.CTkOptionMenu(master=self, values=["normal", "ST-T wave abnormality", "left ventricular hypertrophy"],
                                         command=restecg_callback)
        self.restecg.grid(row=8, column=2, pady=10)

        # ASking for the Maximun heart rate achieved by the user
        self.label9 = customtkinter.CTkLabel(self, text="thalach : \nMaximum heart rate achieved")
        self.label9.grid(row=9, column=1, pady=10)
        self.thalach = customtkinter.CTkEntry(self)
        self.thalach.grid(row=9, column=2, pady=10)

        # Asking for the Excercise-induced angina of the user
        def exang_callback(choice):
            self.exang.set(choice)
        self.label10 = customtkinter.CTkLabel(self, text="exang : \nExercise-induced angina", text_color="black")
        self.label10.grid(row=10, column=1, pady=10)    
        self.exang = customtkinter.CTkOptionMenu(master=self, values=["yes", "no"],
                                         command=exang_callback)
        self.exang.grid(row=10, column=2, pady=10)

        # Asking for the ST depression induced by exercise (relative to rest) of the user
        self.label11 = customtkinter.CTkLabel(self, text="oldpeak : \nST depression induced by exercise \n(relative to rest)")
        self.label11.grid(row=11, column=1, pady=10)
        self.oldpeak = customtkinter.CTkEntry(self)
        self.oldpeak.grid(row=11, column=2, pady=10)

        # Asking for the Slope of the peak exercise ST segment of the user
        def slope_callback(choice):
            self.slope.set(choice)
        self.label12 = customtkinter.CTkLabel(self, text="slope : \nSlope of the peak exercise ST segment", text_color="black")
        self.label12.grid(row=12, column=1, pady=10)    
        self.slope = customtkinter.CTkOptionMenu(master=self, values=["unsloping", "flat", "downsloping"],
                                         command=slope_callback)
        self.slope.grid(row=12, column=2, pady=10)

        # Asking for the ca – Number of major vessels (0–3) colored by fluoroscopy of the user
        self.label11 = customtkinter.CTkLabel(self, text="ca : \nNumber of major vessels \n(0–3) colored by fluoroscopy")
        self.label11.grid(row=13, column=1, pady=10)
        self.ca = customtkinter.CTkEntry(self)
        self.ca.grid(row=13, column=2, pady=10)

        # Asking for the thal – Thalassemia of the user
        def thal_callback(choice):
            self.thal.set(choice)
        self.label14 = customtkinter.CTkLabel(self, text="thal : \nThalassemia", text_color="black")
        self.label14.grid(row=14, column=1, pady=10)    
        self.thal = customtkinter.CTkOptionMenu(master=self, values=["normal", "fixed defect", "reversing defect"],
                                         command=thal_callback)
        self.thal.grid(row=14, column=2, pady=10)
        
        # Button Click
        self.button = customtkinter.CTkButton(self, command=self.button_click, text="Predict", fg_color="black")
        self.button.grid(row=16, column=1, columnspan=2, pady=20)
    
    def button_click(self):
            print("button click")
            name = self.name.get()
            age = self.age.get()
            # sex
            if (self.gender.get() == "male"):
                sex = 1
            else:
                sex = 0
            # cp
            if (self.cp.get()=="typical angina"):
                cp = 0
            elif (self.cp.get()=="atypical angina"):
                cp = 1
            elif (self.cp.get()== "non-anginal pain"):
                cp=2
            else:
                cp=3
            #trestbps    
            trestbps = self.trestbps.get()
            chol = self.chol.get()
            #fbs 
            if (self.fbs.get()=="true"):
                fbs=1
            else: 
                fbs=0
            # restecg 
            if (self.restecg.get()=="normal"):
                restecg = 0
            elif (self.restecg.get()=="ST-T wave abnormality"):
                restecg = 1
            else:
                restecg = 2
            thalach = self.thalach.get()
            # exang
            if (self.exang.get()=="yes"):
                exang = 1
            else:
                exang = 0
            oldpeak = self.oldpeak.get()
            #slope
            if (self.slope.get()=="unsloping"):
                slope = 0
            elif (self.slope.get()=="flat"):
                slope = 1
            else:
                slope = 2
            ca = self.ca.get()
            #thal
            if (self.thal.get()=="normal"):
                thal = 1
            elif (self.thal.get()=="fixed defect"):
                thal = 2
            else:
                thal = 3

            # now proccessing the result to the model
            manual_input = {
                'age': age,
                'sex': sex,
                'cp': cp,
                'trestbps': trestbps,
                'chol': chol,
                'fbs': fbs,
                'restecg': restecg,
                'thalach': thalach,
                'exang': exang,
                'oldpeak': oldpeak,
                'slope': slope,
                'ca': ca,
                'thal': thal
            }
            # convert to DataFrame (1 row)
            input_df = pd.DataFrame([manual_input])
            # prediction
            prediction = loaded_pickle_model.predict(input_df)
            if prediction[0]==1:
                messagebox.showinfo("Prediction", f"{name} there is `RISK`!")
            else:
                messagebox.showinfo("Information", f"{name} therr is `NO RISK`!")
            print(prediction)

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color = "white")

        # Configure the grid system: make the column expand when the window is resized
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        
        #Main Heading
        self.label = customtkinter.CTkLabel(self, text="Fill The Details Below",fg_color="black", text_color="white")
        self.label.grid(row=0, column=0, sticky="nsew",columnspan=1)
        
        myScrollable = MyScrollFrame(self)
        myScrollable.grid(row=1, column=0, sticky="nsew")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Heart Disease Risk Prediction")

        self.myframe = MyFrame(master=self)
        self.myframe.pack(fill="both", expand=True)

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = App()
app.mainloop()