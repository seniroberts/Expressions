class Calendar:
    _workingHours = {"Monday": "uavailable", "Tuesday": "available", "Wednesday": "available",
                     "Thursday": "available", "Friday": "available", "Saturday": "available"}

    def __init__(self, _workingHours) -> dict:
        self._workingHours = _workingHours

    def showAvailableDays(self) -> dict:
        return self._workingHours

    def addNewAvailableTimeSlot(self, day: str, status: str):
        newTimeSlot = {day: status}
        self._workingHours = self._workingHours
        self._workingHours = {** self._workingHours, ** newTimeSlot}
        return self._workingHours

    def getAvailableTimeSlots(self, slotReserved: str) -> dict:
        avaliableDays = {
            key: value for key, value in self._workingHours.items() if value == "available"}
        return avaliableDays

    def isSlotAvailable(self, proposedSlot: str) -> dict:
        avaliableDays = self.getAvailableTimeSlots(proposedSlot).keys()
        if proposedSlot in avaliableDays:
            return True
        else:
            return False

    def removeTimeSlot(self, timeSlot: str) -> dict:
        slotToRemove = {key: value for key,
                        value in self._workingHours.items() if key == timeSlot}
        slotkeys = list(slotToRemove.keys())
        slotkeys = slotkeys[0]
        self._workingHours = {
            key: self._workingHours[key] for key in self._workingHours.keys() - {slotkeys}}
        return self._workingHours
