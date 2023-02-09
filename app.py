from tkinter import filedialog, Label
from datetime import datetime
import tkinter as tk
import pandas as pd
import json

class CSVReader():
     def __init__(self):
          self.window = tk.Tk()
          self.window.title("CSV Reader")
          self.window.geometry("400x400")
          self.file_name = None

          #Text Label
          label= Label(self.window, text= "Please select file",
          font=('Helvetica 15 bold'))
          label.pack(pady= 15)

          #File upload button
          button = tk.Button(self.window, text='Upload File', command=self.fileUpload)
          button.pack()

          #Generate report button
          button = tk.Button(self.window, text='Generate report', command=self.generateReport)
          button.pack()
          
          self.window.mainloop()

     def fileUpload(self, event=None):
          self.file_name = filedialog.askopenfilename()
          #Label for select file
          label=Label(self.window, text=f"Please select a file: {self.file_name}",
          font=('Helvetica 10'))
          label.pack()

     def generateReport(self):
          if self.file_name:
               #header for report
               result = f"{'Summary Report For Credit Cards':^10} \n\n"
               result += f"{'Credit Card Type':<20}{'Num. of Cards':^10}{'Percentage':>20}\n"
               #load csv uploaded csv file into data frame
               data_frame = pd.read_csv(f"{self.file_name}")
               #group by to count by type of credit cards
               creditcards = json.loads(data_frame.groupby('Credit Card Type').size().to_json())

               total = 0
               #total number of credit cards
               for key, value in creditcards.items():
                    total += int(value)

               #loop through rows for getting percentages
               for key, value in creditcards.items():
                    result += f"{key:<20} {value:^10} {(round(((value/total) * 100), 2)):>20}%\n"

               timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
               rptFileName = f"report-{(timestamp)}.txt"
               file = open(rptFileName, "a")
               file.write(result)
               file.close()

               Label(self.window, text="Report file successfully generated.").pack()
               
if __name__ == "__main__":
     _CSVReader = CSVReader()
