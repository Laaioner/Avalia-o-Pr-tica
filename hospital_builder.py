from hospital import Hospital

class HospitalBuilder:
    def __init__(self):
        self.hospital = Hospital()

    def with_doctor(self, doctor):
        self.hospital.register_doctor(doctor)
        return self

    def build(self):
        return self.hospital
