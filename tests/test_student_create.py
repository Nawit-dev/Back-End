from faker import Faker

from logger.logger import Logger

faker = Faker()


class TestStudent:
    def test_student_create(self, group, student):
        Logger.info(f"### Step 1. Group created: {group.name}, id={group.id}")
        Logger.info(f"### Step 2. Student created: {student.first_name} {student.last_name}, id={student.id}")

        assert student.group_id == group.id, ("Wrong group id."
                                              f"Actual: '{student.id}', "
                                              f"but expected: '{group.id}'")
