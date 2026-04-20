from faker import Faker
from services.university.models.group_request import GroupDetailRequest, GroupRequest
from services.university.university_services import UniversityService
from utils.soft_assert import SoftAssert

faker = Faker()


class TestGetGroups:
    def test_get_groups(self, university_api_utils_admin):
        university_services = UniversityService(api_utils=university_api_utils_admin)
        group = university_services.creat_group(GroupRequest(name=faker.name()))
        response = university_services.get_groups(GroupDetailRequest(group_id=group.id))

        sa = SoftAssert()

        sa(group.id == response.id, f"Group id {group.id} not found in response ids: {response.id}")
        sa(group.name in response.name, f"Group name '{group.name}' not found in response names: {response.name}")
        sa.finalize()
