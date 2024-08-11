from notification_service import NotificationAdapter

class Doctor:
    def __init__(self, name, notification_service):
        self.name = name
        self.notification_service = NotificationAdapter(notification_service)

    def update(self, patient):
        self.notification_service.notify(patient.name)
