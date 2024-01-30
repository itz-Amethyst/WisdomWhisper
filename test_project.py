from project import print_data, print_in_figlet_way, get_darktide_quotes

def main():
    test_print_data()
    test_print_in_figlet_way()
    test_get_darktide_quotes()

def test_print_data():
    assert print_data("TESF") == None
    assert print_data("fdsfsdfsd325") == None

def test_print_in_figlet_way():
    assert print_data("TESF") == None
    assert print_data("fdsfsdfsd325") == None

def test_get_darktide_quotes():
    assert print_data("TESF") == None
    assert print_data("fdsfsdfsd325") == None

if __name__ == "__main__":
    main()