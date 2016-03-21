"""
File: erapp2.py
Author: Ken Lambert
Editor: Leigh Stauffer
Project 7

GUI-based view for an emergency room scheduler.
"""

from breezypythongui import EasyFrame
from ermodel import ERModel, Patient, Condition

class ERView(EasyFrame):
    """View of the scheduler."""
    
    def __init__(self, model):
        """Sets up the window and widgets."""
        self.model = model
        EasyFrame.__init__(self, "ER Scheduler")
        self.addLabel(text = "Patient name",
                      row = 0, column = 0)
        self.nameFld = self.addTextField(text = "",
                                         row = 0, column = 1)
        self.conditionGrp = self.addRadiobuttonGroup(row = 1, column = 0)
        selectedBtn = self.conditionGrp.addRadiobutton("Fair condition")
        self.conditionGrp.addRadiobutton("Serious condition")
        self.conditionGrp.addRadiobutton("Critical condition")
        self.conditionGrp.setSelectedButton(selectedBtn)
        self.addButton(text = "Schedule patient", row = 1, column = 1,
                       rowspan = 3, command = self.schedule)
        self.addLabel(text = "Current activity", row = 4, column = 0,
                      columnspan = 2, sticky = "NSEW")
        self.outputArea = self.addTextArea("", row = 5, column = 0,
                                           columnspan = 2,
                                           width = 40, height = 10)
        self.treatNextBtn = self.addButton(text = "Treat next",
                                           row = 6, column = 0,
                                           command = self.treatNext,
                                           state = "disabled")
        self.treatAllBtn = self.addButton(text = "Treat all",
                                          row = 6, column = 1,
                                          command = self.treatAll,
                                          state = "disabled")
        
    # Event handling methods
    def schedule(self):
        """Obtains the patient's name and condition, and schedules
        that patient for service."""
        name = self.nameFld.getText()
        if name == "":
            self.messageBox("ERROR", "No named entered.")
            return                            
        condition = self.getCondition()
        self.model.schedule(Patient(name, condition))
        self.outputArea.appendText(name + " is added to the " + \
                                   str(condition) + " list\n")
        self.treatNextBtn["state"] = "normal"
        self.treatAllBtn["state"] = "normal"

    def treatNext(self):
        """Treats the next patient and updates the display."""
        patient = self.model.treatNext()
        self.outputArea.appendText(str(patient) + " is being treated\n")
        if self.model.isEmpty():
            self.treatNextBtn["state"] = "disabled"
            self.treatAllBtn["state"] = "disabled"
    
    def treatAll(self):
        """Treats all the patients."""
        while not self.model.isEmpty():
            self.treatNext()

    def getCondition(self):
        """Returns a Condition object corresponding to
        the selected radio button in the view."""
        text = self.conditionGrp.getSelectedButton()["text"].split()[0]
        if text == "Fair":
            number = 3
        elif text == "Serious":
            number = 2
        else:
            number = 1
        return Condition(number)

if __name__ == "__main__":
    model = ERModel()
    ERView(model).mainloop()
   
