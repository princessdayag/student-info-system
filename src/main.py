from src.services.student_services import StudentService
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

class StudentInformationSystem:
    def __init__(self):
        self.student_service = StudentService()
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        print("\n=== Student Information System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")

        student_data = {
            'name': name,
            'email': email,
            'course': course,
            'year_level': year_level
        }

        try:
            student = self.student_service.add_student(student_data)
            self.logger.info(f"Added student: {student['student_id']}")
            print(f"Student added successfully! ID: {student['student_id']}")
        except Exception as e:
            self.logger.error(f"Error adding student: {e}")
            print("Error adding student.")

    def view_all_students(self):
        print("\n--- All Students ---")
        students = self.student_service.get_all_students()
        if not students:
            print("No students found.")
            return

        for student in students:
            print(f"ID: {student['student_id']}, Name: {student['name']}, "
                  f"Email: {student['email']}, Course: {student['course']}")

    def update_student(self):
        print("\n--- Update Student ---")
        student_id = input("Enter Student ID to update: ")

        update_data = {}
        print("Leave a field blank if you do not want to change it.")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        course = input("Enter new course: ")
        year_level = input("Enter new year level: ")

        if name:
            update_data['name'] = name
        if email:
            update_data['email'] = email
        if course:
            update_data['course'] = course
        if year_level:
            update_data['year_level'] = year_level

        if not update_data:
            print("No updates provided.")
            return

        try:
            updated_student = self.student_service.update_student(student_id, update_data)
            if updated_student:
                print("Student updated successfully!")
                self.logger.info(f"Updated student: {student_id}")
            else:
                print("Student not found.")
        except Exception as e:
            self.logger.error(f"Error updating student: {e}")
            print("Error updating student.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        student_id = input("Enter Student ID to delete: ")

        confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ").lower()
        if confirm == 'y':
            try:
                deleted = self.student_service.delete_student(student_id)
                if deleted:
                    print("Student deleted successfully!")
                    self.logger.info(f"Deleted student: {student_id}")
                else:
                    print("Student not found.")
                    self.logger.warning(f"Attempted to delete non-existent student: {student_id}")
            except Exception as e:
                self.logger.error(f"Error deleting student: {e}")
                print("Error deleting student.")
        else:
            print("Delete operation cancelled.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                student_id = input("Enter Student ID: ")
                student = self.student_service.get_student(student_id)
                if student:
                    print(f"\nStudent Details: {student}")
                else:
                    print("Student not found.")
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()