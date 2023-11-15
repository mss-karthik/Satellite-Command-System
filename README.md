# Satellite-Command-System
**_Description_**

The Satellite Command System is a sophisticated simulation tool for controlling a virtual satellite in orbit. Designed to replicate the core functionalities of a real-world satellite, this system allows users to manipulate satellite orientation, manage solar panel status, and handle data collection processes.

**_Features_**

Orientation Control: Change the satellite's orientation to North, South, East, or West.

Solar Panel Management: Activate or deactivate the solar panels as needed.

Data Collection: Collect data when solar panels are active, simulating real-world satellite operations.

Robust Error Handling: Comprehensive error and exception management to ensure system reliability.

Interactive Command-Line Interface: User-friendly CLI for easy interaction with the satellite system.

**_Technologies Used_**

 Python
 
Logging module for detailed operational logs.

**_Installation and Setup_**

Clone the repository and navigate to the project directory:

git clone https://github.com/yourusername/Satellite-Command-System.git

cd Satellite-Command-System

**_Run the system:_**

python satellite_command_system.py

**_Usage_**

Once the system is running, use the following commands:

rotate [Direction]: Change orientation (North, South, East, West).
    
activatePanels: Activate the satellite's solar panels.
    
deactivatePanels: Deactivate the solar panels.
    
collectData: Collect data if solar panels are active.
    
exit: Exit the system.

Example:


Enter command: rotate East

Enter command: activatePanels

Enter command: collectData

After these commands, the satellite's state would be:

Orientation: "East"

Solar Panels: "Active"

Data Collected: 10
