import pytest
from api.mytarget_client import MyTargetClient


class TestMyTarget:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.client = MyTargetClient()

    def test_segment_creating(self):
        segment_ids_before = self.client.get_all_segments_ids()
        segment_id = self.client.create_segment()
        segment_ids_after = self.client.get_all_segments_ids()
        assert (segment_id not in segment_ids_before) and (segment_id in segment_ids_after)
        self.client.delete_segment(segment_id=segment_id)

    def test_segment_deleting(self):
        segment_id = self.client.create_segment()
        segment_ids_before = self.client.get_all_segments_ids()
        self.client.delete_segment(segment_id=segment_id)
        segment_ids_after = self.client.get_all_segments_ids()
        assert (segment_id in segment_ids_before) and (segment_id not in segment_ids_after)
