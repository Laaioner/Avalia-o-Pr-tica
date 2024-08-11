class Hospital:
  _instance = None

  def __new__(cls):
      if cls._instance is None:
          cls._instance = super(Hospital, cls).__new__(cls)
          cls._instance.patients = []
          cls._instance.doctors = []
      return cls._instance

  def add_patient(self, patient):
      self.patients.append(patient)
      self.notify_doctors(patient)

  def register_doctor(self, doctor):
      self.doctors.append(doctor)

  def notify_doctors(self, patient):
      for doctor in self.doctors:
          doctor.update(patient)
