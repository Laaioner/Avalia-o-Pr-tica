class NotificationService:
  def send_notification(self, message):
      print(f"Sending notification: {message}")


class NotificationAdapter:
  def __init__(self, notification_service):
      self.notification_service = notification_service

  def notify(self, patient_name):
      self.notification_service.send_notification(f"New patient added: {patient_name}")
