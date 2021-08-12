import pytest
from iso import Code, Iso

iso = Iso()


@pytest.fixture
def example_country():
    return Code(short='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004',
                iso3166_2='ISO3166-2:AF', independent='Yes')


def test_internet_domain(example_country):
    assert example_country.internet_domain() == '.af'


def test_find_correct():
    assert iso.find('PL') is not None
    assert iso.find('DE') is not None


def test_find_wrong():
    assert iso.find('DSA') is None
    assert iso.find('XD') is None


def test_check_true():
    assert iso.find('PL')
    assert iso.find('DE')


def test_check_false():
    assert not iso.check('DSA')
    assert not iso.find('XD')


def test_len():
    assert len(iso) == 249


def test_get_item(example_country):
    assert iso[0] == example_country


with pytest.raises(IndexError):
    assert iso[14243]


def test_codes():
    assert len(iso.codes) == 249
    assert isinstance(iso.codes, list)


def test_get_name_correct():
    assert iso.get_name('Poland')
    assert iso.get_name('Germany')


def test_get_name_wrong():
    assert iso.get_name('ISTHISALAND?') is None
    assert iso.get_name('HELLOTHERE') is None


def test_sort_names():
    assert iso.sort_name[0].short == 'Afghanistan'


def test_sort_aplha2():
    assert iso.sort_alpha2[0].short == 'Andorra'


def test_sort_aplha3():
    assert iso.sort_alpha3[0].short == 'Aruba'


def test_sort_numeric():
    assert iso.sort_numeric[0].short == 'Afghanistan'


def test_sort_independence():
    assert iso.sort_independence[0].short == 'ÅlandIslands'
