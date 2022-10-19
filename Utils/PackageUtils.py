from Objects.Package import Package
from Utils.CSVUtils import get_packages_from_csv


def get_packages() -> list:
    packages_from_scv = get_packages_from_csv()
    packages = []
    for package in packages_from_scv:
        package_id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zipcode = package[4]
        deadline = package[5]
        weight = package[6]
        status = "At Hub"

        packages.append(
            Package(address, city, deadline, package_id, state, status, weight, zipcode)
        )

    return packages
