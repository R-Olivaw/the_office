"""

This module contains the office.

"""

class Room:
    
    def __init__(self, name, employee_list):
        """
        
        Summary
        -------
        
        A room within the office. Each room contains workstations and employees assigned to those workstations.
        
        Parameters
        ----------
        
        name : string
            The name of the room (e.g. 'Conference Room')
            
        employee_list : list
            A list containing Employee objects.
        
        """
        
        self.name = name
        self.employee_list = employee_list
    
    def work_station(self):
        work_station_count = 0
        
    
    def description(self):
        pass
    
    def activity(self):
        pass
    
