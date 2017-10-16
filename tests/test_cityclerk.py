from tests.utils import file_response
from documenters_aggregator.spiders.ccc import CccSpider

file = file_response('files/ccc.json')
spider = CccSpider()
file
test_response = file
parsed_items = list(spider.parse(test_response))

for item in parsed_items[0]:
    print(item)
    print(parsed_items[0][item])
print(parsed_items[0]['sources'][0])
print(parsed_items[0]['description'] == '')
print(parsed_items[0]['location'])


def test_name():
    assert parsed_items[0]['name'] == 'Joint Committee: Finance; Transportation and Public Way'


def test_description():
    assert parsed_items[0]['description'] == ''


def test_start_time():
    assert parsed_items[0]['start_time'] == '2017-10-16T15:00:00+00:00'


def test_end_time():
    assert parsed_items[0]['end_time'] == ''


def test_id():
    assert parsed_items[0]['id'] == 'ocd-event/86094f46-cf45-46f8-89e2-0bf783e7aa12'


def test_all_day():
    assert parsed_items[0]['all_day'] is False


def test_classification():
    assert parsed_items[0]['classification'] == 'event'


def test_status():
    assert parsed_items[0]['status'] == 'cancelled'


def test_location():
    assert parsed_items[0]['location'] == {
        "name": "Council Chambers ,  City Hall ",
        "coordinates": None,
        "url": ""
    }


def test_sources():
    assert parsed_items[0]['sources'] == [
                                         {"note": "ocd-api",
                                          "url": "https://ocd.datamade.us/ocd-event/86094f46-cf45-46f8-89e2-0bf783e7aa12"},
                                         {"note": "api",
                                          "url": "http://webapi.legistar.com/v1/chicago/events/4954"},
                                         {"note": "web",
                                          "url": "https://chicago.legistar.com/MeetingDetail.aspx?ID=565455&GUID=B5103C52-1793-4B07-9F28-E0A1223E1540&Options=info&Search="}
    ]


def test__type():
    assert parsed_items[0]['_type'] == 'event'
