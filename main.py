from hospital_builder import HospitalBuilder
from doctor import Doctor
from notification_service import NotificationService
from patient import Patient

if __name__ == "__main__":
    # Criar um serviço de notificação
    notification_service = NotificationService()

    # Construir o hospital
    hospital_builder = HospitalBuilder()
    hospital = hospital_builder.with_doctor(Doctor("Dr. Smith", notification_service)).build()

    # Adicionar pacientes
    patient1 = Patient("Alice")
    hospital.add_patient(patient1)

    patient2 = Patient("Bobbs")
    hospital.add_patient(patient2)

    # Listar pacientes
    print("Patients in the hospital:")
    for patient in hospital.patients:
        print(f"- {patient.name}")
