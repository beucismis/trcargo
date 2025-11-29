import argparse
import inspect
import pkgutil

from rich.pretty import pprint

import trcargo.companies
from trcargo.companies import base


def main():
    parser = argparse.ArgumentParser(description="Track packages from Turkish cargo companies.")
    parser.add_argument("company", help="Cargo company name.")
    parser.add_argument("query", help="Tracking number or query.")
    args = parser.parse_args()

    company_name = args.company.lower()
    query = args.query
    cargo_company = None

    for importer, modname, ispkg in pkgutil.iter_modules(trcargo.companies.__path__, f"{trcargo.companies.__name__}."):
        module = __import__(modname, fromlist="dummy")

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, base.BaseCompaine) and obj is not base.BaseCompaine:
                if obj.NAME.lower().startswith(company_name):
                    cargo_company = obj()
                    break

        if cargo_company:
            break

    if cargo_company:
        try:
            result = cargo_company.get_search(query)
            pprint(result)
        except base.CargoTrackingError as e:
            print(f"Error: {e}")
    else:
        print(f"Company '{args.company}' not found.")


if __name__ == "__main__":
    main()
