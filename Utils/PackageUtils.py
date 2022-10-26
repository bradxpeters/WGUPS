from Objects.Constants import AT_HUB
from Objects.Package import Package
from Utils.CSVUtils import get_packages_from_csv


def get_packages() -> list:
    packages_from_scv = get_packages_from_csv()
    packages = []
    for package in packages_from_scv:
        address = package[1]
        city = package[2]
        deadline = package[5]
        package_id = int(package[0])
        state = package[3]
        status = AT_HUB
        weight = package[6]
        zipcode = package[4]

        packages.append(
            Package(address, city, deadline, package_id, state, status, weight, zipcode)
        )

    return packages
