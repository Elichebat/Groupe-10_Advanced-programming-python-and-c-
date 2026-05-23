
from person import Person  # type: ignore # Import of the parent class


class Student(Person):

    def __init__(self, last_name, first_name, id, field_of_study, entry_time, exit_time):
        # Call the parent constructor via super()
        super().__init__(last_name, first_name, id)

        # Attributes specific to Student
        self.field_of_study = field_of_study
        self.entry_time = entry_time   
        self.exit_time  = exit_time    

        # is_late: True if the student arrived after 8h00
        # We convert "HHhMM" to total minutes to compare
        # Example: "08h30" -> 8*60 + 30 = 510 minutes > 480 (8h00) -> late
        self.is_late = self._convert_to_minutes(entry_time) > self._convert_to_minutes("08h00")

    def _convert_to_minutes(self, time_str):
        # Splits "08h30" into ["08", "30"], then converts to total minutes
        parts   = time_str.split("h")
        hours   = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
