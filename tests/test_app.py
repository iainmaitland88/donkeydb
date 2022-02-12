from src.app import DonkeyDB


def test_can_insert_and_get_data():
    db = DonkeyDB()
    key1 = db.insert("foo")
    key2 = db.insert("bar")

    assert "bar" == db.get(key2)
    assert "foo" == db.get(key1)
