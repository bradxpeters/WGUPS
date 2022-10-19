from Utils.CSVUtils import get_addresses_from_csv


def get_address(address):
    addresses = get_addresses_from_csv()
    for row in addresses:
        if address in row[2]:
            return int(row[0])
